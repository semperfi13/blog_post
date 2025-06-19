from django import template
from ..models import Post

# We have created a simple template tag that returns the number of posts
# published on the blog.
register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()
