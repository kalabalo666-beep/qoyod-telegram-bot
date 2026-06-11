#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
إعدادات التطبيق
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()


class Config:
    """فئة الإعدادات الأساسية"""
    
    # Telegram
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("❌ TELEGRAM_BOT_TOKEN غير موجود في .env")
    
    # Qoyod API
    QOYOD_API_KEY = os.getenv("QOYOD_API_KEY")
    if not QOYOD_API_KEY:
        raise ValueError("❌ QOYOD_API_KEY غير موجود في .env")
    
    QOYOD_API_URL = os.getenv("QOYOD_API_URL", "https://api.qoyod.com/api/v2")
    
    # Google Drive
    GOOGLE_DRIVE_FOLDER_ID = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
    GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON", "./google-credentials.json")
    
    # Database
    DB_PATH = os.getenv("DB_PATH", "./data/raed.db")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "./logs/bot.log")
    
    # Company Info
    COMPANY_NAME = os.getenv("COMPANY_NAME", "شركة رائد")
    COMPANY_ID = os.getenv("COMPANY_ID", "raed_company")
    
    # Create necessary directories
    @staticmethod
    def ensure_directories():
        """إنشاء المجلدات الضرورية"""
        Path("data").mkdir(exist_ok=True)
        Path("logs").mkdir(exist_ok=True)
        Path("downloads").mkdir(exist_ok=True)


def load_config():
    """تحميل الإعدادات والتحقق من الملفات الضرورية"""
    Config.ensure_directories()
    return Config
