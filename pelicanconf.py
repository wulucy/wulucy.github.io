#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lucy Wu'
SITENAME = "Lucy's Blog"
SITETITLE = 'Lucy Wu'
SITEURL = 'https://wulucy.github.io'
#SITEICON = 'https://lh3.google.com/u/1/d/13KatGZwHDdX31FVz5ZQqjoJQC5des7N7=w2560-h1452-iv1'
SITEICON = SITEURL + '/images/favicon.ico'
SITELOGO = SITEURL + '/images/headshot-bw2.JPG'
PATH = 'content'
STATIC_PATHS = ['images', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'}}

TIMEZONE = 'America/New_York'
COPYRIGHT_YEAR = '2018'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HOME_HIDE_TAGS = True
DATE_FORMATS = {
    'en': '%B %d, %Y',
}
# Blogroll
#LINKS = (('GitHub', 'http://github.com/wulucy/'),
#         ('LinkedIn', 'https://www.linkedin.com/in/lucy-wu-741392126/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/wulucy'),
          ('linkedin', 'https://www.linkedin.com/in/lucy-wu-741392126'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

#PLUGIN_PATH = '/Users/lucy/pelican-themes/voce/plugins/'
#PLUGINS = ['ipynb.markup', 'assets']
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = '/Users/lucy/pelican-themes/Flex'
>>>>>>> Stashed changes
