#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

omikuji = [u'大吉', u'中吉', u'吉', u'凶']
res = omikuji[random.randint(0, 3)]

template = '''
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>Omikuji</title>
</head>
<body>
  <p>{}</p>
</body>
</html>
'''

print "Content-Type: text/html"
print
print template.format(res)
