from django.contrib import admin

# Register your models here.
from .models import NhaSanXuat, MatHang
class NSTAdmin(admin.ModelAdmin):
    list_display= ('id', 'name')
class SPAdmin(admin.ModelAdmin):
    list_display= ('ma_sp','ten_sp','gia')
admin.site.register(NhaSanXuat, NSTAdmin)
admin.site.register(MatHang, SPAdmin)

admin.site.site_header = ('Quản lí sản phẩm')