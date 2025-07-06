#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
局域网安全操作规范视频分享系统
主程序文件
"""

import os
import sqlite3
import json
import time
from datetime import datetime, timedelta
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import secrets
import mimetypes
import logging
from contextlib import contextmanager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size

# 配置路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置日志
log_file = os.path.join(BASE_DIR, '.runtime', 'app.log')
os.makedirs(os.path.dirname(log_file), exist_ok=True)
handler = logging.FileHandler(log_file) # 输出到文件
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
STATIC_DIR = os.path.join(BASE_DIR, 'static')
VIDEOS_DIR = os.path.join(BASE_DIR, 'videos')
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')
THUMBNAILS_DIR = os.path.join(BASE_DIR, 'thumbnails')
CAROU