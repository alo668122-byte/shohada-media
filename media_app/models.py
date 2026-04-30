from django.db import models

class MediaCategory(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام دسته‌بندی")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.name

class MediaFile(models.Model):
    MEDIA_TYPES = [
        ('image', 'عکس'),
        ('audio', 'صوت'),
        ('video', 'فیلم'),
    ]

    title = models.CharField(max_length=300, verbose_name="عنوان")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, verbose_name="نوع رسانه")
    file = models.FileField(upload_to='media_files/', verbose_name="فایل")
    category = models.ForeignKey(
        MediaCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="دسته‌بندی"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ آپلود")

    class Meta:
        verbose_name = "فایل رسانه"
        verbose_name_plural = "فایل‌های رسانه"
        ordering = ['-created_at']

    def __str__(self):
        return self.title