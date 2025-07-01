# A sitemap is an XML file that tells
# search engines the pages of your website, their relevance, and how
# frequently they are updated. Using a sitemap will make your site morevisible in search
# engine rankings because it helps crawlers to index your
# website’s content.

from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated
