# Gunicorn 配置文件

# 绑定地址和端口
bind = "0.0.0.0:8081"

# 工作进程数
workers = 4

# 工作进程类型
worker_class = "sync"

# 每个工作进程的线程数
threads = 2

# 工作进程最大请求数
max_requests = 1000
max_requests_jitter = 100

# 超时设置
timeout = 120
keepalive = 5

# 日志配置
accesslog = "logs/access.log"
errorlog = "logs/error.log"
loglevel = "info"

# 进程名称
proc_name = "safety_video_platform"

# 预加载应用
preload_app = True

# 用户和组（如果需要）
# user = "www-data"
# group = "www-data"

# PID 文件
pidfile = "logs/gunicorn.pid"

# 临时目录
tmp_upload_dir = None

# 启用访问日志
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# 工作进程重启
max_requests = 1000
max_requests_jitter = 100

# 内存限制
worker_tmp_dir = "/dev/shm"

# 优雅重启
graceful_timeout = 30