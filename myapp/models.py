from django.db import models

# Create your models

class NhaSanXuat(models.Model):
    name = models.CharField(max_length=200, verbose_name='Tên')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Nhà Sản Xuất'
        verbose_name_plural = 'Nhà Sản Xuất'

class MatHang(models.Model):
    ma_sp = models.CharField(max_length = 200, default =True,verbose_name='Mã sp')
    ten_sp = models.CharField(max_length = 200, default=True,verbose_name='Tên sp')
    gia = models.CharField(max_length = 200, default = True, verbose_name='Giá')
    nhasanxuat = models.ManyToManyField(NhaSanXuat)

    def __str__(self):
        return self.ten_sp
    class Meta:
        verbose_name = 'Sản Phẩm'
        verbose_name_plural ='Sản Phẩm'



