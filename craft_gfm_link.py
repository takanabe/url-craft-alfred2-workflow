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
from workflow import Workflow,web

def main(wf):
    # Get args from Workflow, already in normalised Unicode

    query = None  # Ensure `query` is initialised
    # Set `query` if a value was passed (it may be an empty string)
    if len(wf.args):
       query = wf.args[0]

    url = query

    #=========================================================#
    # title: it shows a big sentence in result
    # subtitle : it shows a small sentence in result
    # valid : valid = True tells Alfred that the item is actionable
    # arg : the value it will pass to the next action
    #=========================================================#

    wf.add_item(title = 'Craft URL as GFM style',subtitle = url, valid = True, arg = url,icon = 'icon.png')
    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
