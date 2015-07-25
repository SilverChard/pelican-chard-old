#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#作者 站名 地址等信息
AUTHER = u"Silver Chard"
SITENAME = u"Silver's Blog"
SITEURL = 'http://silverchard.me'

#主题等
PATH = 'content'
THEME = '/usr/lib/python2.7/site-packages/pelican-3.6.0-py2.7.egg/pelican/themes/pelican-chard'


#使用目录名作为文章的分类名
USE_FOLDER_AS_CATEGORY = True

#时间格式 时区等
TIMEZONE = 'Asia/Shanghai'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M'

#默认语言
DEFAULT_LANG = u'zh'

# 各种常用feed 全～没～用～
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# 友情链接
# Blogroll
LINKS = (('张骞', 'http://mcdona1d.me/'),
         ('刘亚龙', 'http://kidyalong.com/'),)

#社交账号
# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/ChardShieh'),
          ('Google+', 'https://plus.google.com/+SilverChard'),
          ('twitter', 'https://twitter.com/Silver_Xie'),
          ('QQ', 'http://user.qzone.qq.com/330680229'),
          ('Weibo', 'http://weibo.com/1843103547'),)


#默认分页页码
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


#导入partial包 服务于pelican-chard
from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order

        

#使用文件名作为文章或页面的slug
FILENAME_METADATA = '(?P<slug>.*)'

#页面的显示路径和保存路径
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
#隐藏后缀
READERS = {'html': None}

#插件
PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = [
          'sitemap',
		      'tipue_search',
          'liquid_tags.img', 
          'liquid_tags.notebook',
          ]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

#静态文件目录拷贝
EXTRA_PATH_METADATA = (
    ("extra/robots.txt", "robots.txt"),
    ("extra/generate_204", "generate_204"),
)
STATIC_PATHS = [u"img"]