#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
بوت تيليجرام قيود - شركة رائد
Main entry point للتطبيق
"""

import logging
import sys
from pathlib import Path

# إضافة المجلد الرئيسي للمسار
sys.path.insert(0, str(Path(__file__).parent))

from config.settings import load_config
from bot.telegram_bot import QoyodBot
from utils.logger import setup_logger

# إعداد التسجيل
logger = setup_logger(__name__)


def main():
    """نقطة الدخول الرئيسية للبوت"""
    try:
        logger.info("🤖 جاري بدء بوت قيود - شركة رائد...")
        
        # تحميل الإعدادات
        config = load_config()
        logger.info(f"✅ تم تحميل الإعدادات بنجاح")
        
        # إنشاء وتشغيل البوت
        bot = QoyodBot(config)
        logger.info("✅ تم إنشاء البوت بنجاح")
        
        logger.info("🚀 بدء استقبال الرسائل...")
        bot.start()
        
    except Exception as e:
        logger.error(f"❌ خطأ في البوت: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
