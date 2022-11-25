from django.contrib import admin
from .models import Comment,Post

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'name', 'email', 'body', 'created', 'updated', 'active', )
    list_display_links = ('id', 'post')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status', )
    list_display_links = ('id', 'title')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author', )
    date_hierarchy = 'publish'
    ordering = ('status', 'publish', )


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
