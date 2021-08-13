# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import datetime, timedelta

class Comment(models.Model):

    # Support integer and UUID primary keys
    object_id = models.CharField(
        max_length=36  # 36 chosen to match UUID length (RFC4122)
    )

    content_object = GenericForeignKey(
        "content_type",
        "object_id"
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=False,
        null=True
    )

    time = models.DateTimeField(
        auto_now_add=True
    )

    comment = models.TextField(
        blank=False
    )

    email_sent = models.BooleanField(default=False)

    def __str__(self):
        self.time = self.time + timedelta(hours=2)
        return self.time.strftime("%b. %d, %Y, %-I:%M %p")


__all__ = ['Comment']
