#!/usr/bin/python
# encoding: utf-8

'''
URL Craft v0.1.0

Github : https://github.com/takanabe/url-craft-alfred2-workflow
Author : takanabe (taknabe.w@gmail.com)
Twitter: @takanabe_w
Blog   : http://blog.takanabe.tokyo
'''

import sys
import re
import urllib2
from workflow import Workflow,web

def main(wf):
    # Get args from Workflow, already in normalised Unicode
    query = None  # Ensure `query` is initialised
    # Set `query` if a value was passed (it may be an empty string)
    if len(wf.args):
       query = wf.args[0]

    url = query

    res = urllib2.urlopen(url)
    pattern_title = re.compile('<title>(.*?)</title>')
    m = pattern_title.search(res.read())
    title = m.group(1)

    print "[{title}]({url})".format(title = title, url = url)

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))

