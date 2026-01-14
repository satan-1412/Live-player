from flask import Flask, request, jsonify
import yt_dlp
import time

app = Flask(__name__)

@app.route('/api/check', methods=['GET'])
def check_url():
    # 1. 获取链接
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "请提供链接"}), 400

    # 2. 针对移动端和 Vercel 的极限优化配置
    ydl_opts = {
        # --- 性能与超时 ---
        'socket_timeout': 9,        # 设置为 9 秒，留 1 秒给 Flask 返回错误信息，防止 Vercel 强制杀后台
        'retries': 3,               # 网络波动时重试 3 次（针对手机信号差）
        'fragment_retries': 3,      # 视频分片重试
        
        # --- 核心解析设置 ---
        'simulate': True,           # 核心：只模拟，绝对不下载
        'skip_download': True,      # 核心：跳过下载
        'force_json': True,         # 强制 JSON
        'extract_flat': True,       # 如果是播放列表，不深挖每一集，只抓列表（极大提升速度）
        
        # --- 网络兼容性 ---
        'nocheckcertificate': True, # 跳过 SSL 验证（部分小网站证书过期也能抓）
        'source_address': '0.0.0.0',# 强制使用 IPv4（避免部分服务器 IPv6 路由慢的问题）
        'quiet': True,
        'no_warnings': True,
        
        # --- 伪装设置 ---
        # 伪装成 iPhone 手机访问，很多网站对手机端防爬策略较松
        'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    }

    start_time = time.time()
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 提取信息
            info = ydl.extract_info(url, download=False)
            
            # 计算耗时
            elapsed = round(time.time() - start_time, 2)

            # 3. 数据清洗（只返回前端需要的数据，节省流量）
            formats_found = []
            
            # 处理 formats (视频流)
            if 'formats' in info:
                for f in info['formats']:
                    # 筛选逻辑：保留 m3u8 或者有分辨率的，排除纯音频
                    if f.get('resolution') != 'audio only' or 'm3u8' in f.get('protocol', '') or f.get('ext') == 'm3u8':
                        # 格式化画质标签
                        note = f.get('format_note')
                        res = f.get('resolution')
                        height = f.get('height')
                        
                        label = "未知"
                        if note: label = str(note)
                        elif res: label = str(res)
                        elif height: label = f"{height}p"
                        
                        formats_found.append({
                            "resolution": label,
                            "ext": f.get('ext'),
                            "proto": f.get('protocol', 'unknown')
                        })

            return jsonify({
                "status": "success",
                "time_cost": f"{elapsed}s",
                "title": info.get('title', 'Unknown Title'),
                "extractor": info.get('extractor', 'Unknown'),
                "formats": formats_found
            })

    except Exception as e:
        error_msg = str(e)
        # 优化错误提示，让用户看懂
        if "time" in error_msg.lower() or "out" in error_msg.lower():
            return jsonify({"error": "解析超时 (超过9秒)。源站响应太慢，或 Vercel 免费版限制。"}), 504
        elif "geo" in error_msg.lower():
            return jsonify({"error": "该视频限制地区播放。"}), 403
        else:
            # 截取短一点的错误信息
            return jsonify({"error": f"解析失败: {error_msg[:100]}..."}), 500

# Vercel 需要这个
app.debug = False
