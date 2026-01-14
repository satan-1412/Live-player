<div align="center">

# 📺 M3U/M3U8 Web Toolbox
### 下一代可视化直播源管理与监测平台

<p align="center">
  <a href="https://github.com/satan-1412/Live-tool/stargazers">
    <img src="https://img.shields.io/github/stars/satan-1412/Live-tool?style=for-the-badge&logo=github&color=yellow" alt="Stars">
  </a>
  <a href="https://github.com/satan-1412/Live-tool/network/members">
    <img src="https://img.shields.io/github/forks/satan-1412/Live-tool?style=for-the-badge&logo=github&color=orange" alt="Forks">
  </a>
  <a href="https://github.com/satan-1412/Live-tool/issues">
    <img src="https://img.shields.io/github/issues/satan-1412/Live-tool?style=for-the-badge&logo=github&color=red" alt="Issues">
  </a>
  <a href="https://github.com/satan-1412/Live-tool/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/satan-1412/Live-tool?style=for-the-badge&logo=github&color=blue" alt="License">
  </a>
</p>

<p align="center">
    <a href="https://satan-1412.github.io/Live-tool/">
        <img src="https://img.shields.io/badge/🚀_在线演示-Live_Demo-success?style=for-the-badge" alt="Live Demo">
    </a>
</p>

<p align="center">
  <a href="#-项目概述">项目概述</a> •
  <a href="#-核心特性">核心特性</a> •
  <a href="#-技术架构">技术架构</a> •
  <a href="#-快速部署">快速部署</a> •
  <a href="#-国际化">多语言支持</a>
</p>

</div>

---

## 📖 项目概述

**M3U/M3U8 Web Toolbox** 是一款基于现代 Web 标准构建的**轻量级、零依赖、纯前端**直播源综合管理解决方案。

专为 IPTV 爱好者、运维人员及开发者设计，它集成了**高并发链路检测**、**可视化播放列表编排**、**格式无损转换**及**HLS 流媒体预览**四大核心能力。项目采用单文件架构（Single-File Component），无需复杂的后端环境，即开即用，并在浏览器端通过本地运行时（Local Runtime）保障数据隐私与安全。

## ✨ 核心特性

### 1. 📝 可视化编排引擎 (Visual Orchestration)
抛弃繁琐的文本编辑器，提供所见即所得的交互体验。
- **拖拽排序**：基于 `SortableJS` 实现流畅的频道拖拽排序。
- **多视图切换**：支持传统的**列表视图**与现代化的**网格卡片视图**。
- **批量作业**：支持批量修改分组（Group）、台标（Logo）及批量删除，大幅提升维护效率。
- **智能补全**：内置模板引擎，快速追加频道属性。

### 2. 📡 智能连通性探测 (Intelligent Connectivity Probe)
采用启发式算法对直播源进行健康度检查。
- **高并发队列**：支持多线程并发检测，快速处理大规模列表。
- **混合探测模式**：首选 HEAD 请求，失败时自动降级为 GET 请求，并利用 `no-cors` 策略探测服务器存活状态，有效解决跨域误报问题。
- **实时反馈**：毫秒级响应时间显示，精准区分“有效”、“疑似有效（CORS限制）”与“无效”状态。

### 3. 🔄 全格式互操作性 (Interoperability)
打破格式壁垒，支持主流 IPTV 格式间的无缝流转。
- **输入/输出**：支持 M3U, M3U8, TXT, JSON, TiviMate 扩展格式。
- **智能清洗**：在转换过程中自动剔除无效字段，优化文件体积。
- **TiviMate 优化**：针对 TiviMate 播放器自动补全 `tvg-id` 等关键元数据。

### 4. 📺 HLS 流媒体预览 (Instant Preview)
- **原生内核**：集成 `hls.js` 最新版内核，支持 HLS (HTTP Live Streaming) 协议。
- **极速秒开**：优化的缓冲策略，实现点击即播。
- **移动端适配**：完美适配 iOS/Android 原生播放器手势。

---

## 🛠 技术架构

本项目遵循 **KISS (Keep It Simple, Stupid)** 原则，采用现代原生技术栈构建：

| 模块 | 技术选型 | 说明 |
| :--- | :--- | :--- |
| **Core** | HTML5 / ES6+ | 纯原生实现，无 Webpack/Vite 打包负担 |
| **Styling** | CSS Variables | 支持动态主题与响应式布局 (Mobile First) |
| **Streaming** | hls.js | 企业级 HLS 流媒体解码库 |
| **Interaction** | SortableJS | 高性能拖拽交互库 |
| **UI Design** | Glassmorphism | 沉浸式暗黑风格与玻璃拟态设计 |

---

## 🌍 国际化支持 (i18n)

内置强大的国际化引擎，根据用户浏览器设置自动适配，支持 **9 种语言** 实时热切换：

| 区域 | 语言 | 标识 |
| :--- | :--- | :--- |
| 🇨🇳 | **简体中文** | zh-CN |
| 🇺🇸 | **English** | en-US |
| 🇯🇵 | **日本語** | ja-JP |
| 🇰🇷 | **한국어** | ko-KR |
| 🇷🇺 | **Русский** | ru-RU |
| 🇩🇪 | **Deutsch** | de-DE |
| 🇫🇷 | **Français** | fr-FR |
| 🇪🇸 | **Español** | es-ES |
| 🇧🇷 | **Português** | pt-BR |

---

## 🚀 快速部署

由于本项目采用了 **Single-File (单文件)** 架构，部署极其简单。

### 方式一：GitHub Pages (推荐)
直接 Fork 本仓库，并在 Repository Settings 中开启 GitHub Pages，即可获得与演示站点一致的体验。

### 方式二：本地运行
下载仓库中的 `index.html` 文件，直接双击使用浏览器打开即可。

### 方式三：Docker / Nginx
```bash
# 1. 克隆仓库
git clone [https://github.com/satan-1412/Live-tool.git](https://github.com/satan-1412/Live-tool.git)

# 2. 将 index.html 放入任意 Web 服务器根目录
cp Live-tool/index.html /usr/share/nginx/html/

🛡️ 隐私与安全声明
我们深知直播源列表可能包含敏感信息（如 Token、私有服务器地址）。
> 🔒 零数据上传承诺：
> M3U Web Toolbox 是一个纯客户端应用（Client-Side App）。所有的文件解析、编辑、检测逻辑均在您的浏览器本地内存中执行。本项目没有任何后端服务器，不会收集、上传或存储您的任何播放列表数据。
> 
🤝 贡献指南 (Contributing)
我们欢迎社区贡献代码，共同打造最强 Web 端直播源工具。
 * Fork 本仓库
 * 创建特性分支 (git checkout -b feature/AmazingFeature)
 * 提交更改 (git commit -m 'Add some AmazingFeature')
 * 推送到分支 (git push origin feature/AmazingFeature)
 * 提交 Pull Request
<div align="center">
<p>如果这个项目对您有帮助，请不吝点亮右上角的 ⭐️ Star！</p>
<sub>Designed & Built by <a href="https://www.google.com/search?q=https://github.com/satan-1412">satan-1412</a></sub>


<img src="https://www.google.com/search?q=https://img.shields.io/github/last-commit/satan-1412/Live-tool%3Fstyle%3Dflat-square%26color%3Dlightgrey" alt="Last Commit">
</div>

