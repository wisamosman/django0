from django.contrib import admin
from .models import Post , Author

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date']
    list_filter = ['author', 'publish_date', 'tags']
    search_fields = ['title', 'content']


admin.site.register(Post,PostAdmin)
admin.site.register(Author)

# Register your models here.



