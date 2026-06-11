#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
بوت تيليجرام الرئيسي
"""

import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from bot.handlers import (
    start_command,
    help_command,
    upload_command,
    invoices_command,
    entries_command,
    status_command,
    document_handler,
    text_handler,
    error_handler
)

logger = logging.getLogger(__name__)


class QoyodBot:
    """فئة البوت الرئيسية"""
    
    def __init__(self, config):
        """تهيئة البوت
        
        Args:
            config: كائن الإعدادات
        """
        self.config = config
        self.app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
        self._setup_handlers()
    
    def _setup_handlers(self):
        """إعداد معالجات الأوامر والرسائل"""
        # أوامر
        self.app.add_handler(CommandHandler("start", start_command))
        self.app.add_handler(CommandHandler("help", help_command))
        self.app.add_handler(CommandHandler("upload", upload_command))
        self.app.add_handler(CommandHandler("invoices", invoices_command))
        self.app.add_handler(CommandHandler("entries", entries_command))
        self.app.add_handler(CommandHandler("status", status_command))
        
        # معالجات الرسائل
        self.app.add_handler(MessageHandler(filters.Document.ALL, document_handler))
        self.app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
        
        # معالج الأخطاء
        self.app.add_error_handler(error_handler)
    
    def start(self):
        """بدء البوت"""
        logger.info("🚀 جاري بدء البوت...")
        self.app.run_polling()
