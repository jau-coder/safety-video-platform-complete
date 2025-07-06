# 安全操作规范视频库

一个功能完整的局域网视频分享系统，专为企业内部安全培训和操作规范视频管理而设计。

## 🎯 功能特性

### 核心功能
- **视频管理**: 支持多格式视频上传、播放、分类管理
- **用户系统**: 完整的用户注册、登录、权限控制
- **观看体验**: 自动生成缩略图、观看历史记录、收藏功能
- **内容管理**: 轮播图管理、分类管理、视频信息编辑
- **管理面板**: 用户管理、统计数据、系统监控

### 技术特性
- **响应式设计**: 支持桌面端和移动端访问
- **高性能**: 基于Flask + Gunicorn + SQLite的轻量级架构
- **容器化部署**: 支持Docker一键部署
- **安全可靠**: 完整的权限控制和数据验证

## 🏗️ 技术架构

- **后端**: Python Flask 框架
- **数据库**: SQLite (轻量级，免维护)
- **前端**: HTML5 + CSS3 + JavaScript (原生)
- **视频处理**: FFmpeg (缩略图生成)
- **部署**: Docker + Gunicorn

## 📁 项目结构

```
safety-video-platform/
├── app.py                 # 主应用程序
├── requirements.txt       # Python依赖
├── Dockerfile            # Docker配置
├── docker-compose.yml    # Docker Compose配置
├── gunicorn.conf.py      # Gunicorn配置
├── templates/            # HTML模板
│   ├── index.html        # 主页
│   ├── player.html       # 视频播放页
│   ├── admin.html        # 管理面板
│   └── ...
├── static/               # 静态资源
│   ├── css/             # 样式文件
│   └── js/              # JavaScript文件
├── videos/              # 视频文件目录
├── thumbnails/          # 缩略图目录
├── uploads/             # 上传临时目录
├── carousel/            # 轮播图目录
├── database/            # 数据库目录
└── logs/               # 日志目录
```

## 🚀 快速开始

### 方式一：Docker部署（推荐）

1. **克隆项目**
```bash
git clone https://github.com/jau-coder/safety-video-platform-complete.git
cd safety-video-platform-complete
```

2. **启动服务**
```bash
docker-compose up -d
```

3. **访问系统**
- 打开浏览器访问: http://localhost:8081
- 默认管理员账户: admin / admin123

### 方式二：本地部署

1. **环境要求**
- Python 3.8+
- FFmpeg

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **启动应用**
```bash
python app.py
```

## ⚙️ 详细配置

### 环境变量配置

创建 `.env` 文件：
```bash
# 应用配置
SECRET_KEY=your-secret-key-here
FLASK_ENV=production
PORT=8081

# 数据库配置
DATABASE_PATH=database/videos.db

# 文件路径配置
VIDEOS_DIR=videos
UPLOADS_DIR=uploads
THUMBNAILS_DIR=thumbnails
CAROU