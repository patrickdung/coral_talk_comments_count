# -*- coding: utf-8 -*-

# SPDX-License-Identifier: AGPL-3.0-only
#
# Copyright (c) 2022 Patrick Dung

from __future__ import unicode_literals
import base64
import urllib.request
import re

##from pelican import signals, contents, generators, settings
from pelican import signals

"""
  This plugin is for getting the comments count of an article (Coral Talk)
"""

def article_url(content):
  return SITEURL+'/'+content.url
  ##return PROD_SITEURL+'/'+content.url

def initialize_module(pelican):
  global SITEURL, CORAL_DOMAIN_NAME

  for parameter in [ 'SITEURL', 'CORAL_DOMAIN_NAME' ]:
    if not parameter in pelican.settings.keys():
        print ("Error: " + parameter + "not defined in settings")
    else:
      globals()[parameter] = pelican.settings.get(parameter)

class Comments(object):
  def __init__(self):
    self.count = 0

def setup_comments_count(generator, metadata):
  metadata['coral_comments'] = Comments()

def get_comments_count(generator, content):
  try:
    target_url = article_url(content)
    coral_query_string = 'false;'+target_url

    coral_ref_message_bytes = coral_query_string.encode("ascii")
    coral_ref_base64_bytes = base64.b64encode(coral_ref_message_bytes)
    coral_ref_base64_encoded = coral_ref_base64_bytes.decode("ascii")
    # print (coral_ref_base64_encoded)

    coral_query_url = 'https://' + CORAL_DOMAIN_NAME + '/api/story/count.js?callback=CoralCount.setCount&notext=false&ref=' + coral_ref_base64_encoded + '&url=' + target_url
    # print (coral_query_url)
    ## Coral count.js needs user-agent
    ##response = urllib.request.urlopen(coral_query_url)
    req = urllib.request.Request(coral_query_url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    data = response.read().decode("utf-8")
    #print (str(data))
    p = re.compile('"count":(.*),"id"')
    result = p.findall(str(data))
    # print (p.findall(str(data)))
  except:
    raise

  if result:
    # findall return a list
    content.coral_comments.count = result[0]
  return (result)

def register():
    ## only need to add to the global before writing article/pages/templates
    signals.initialized.connect(initialize_module)

    ## only works for articles
    signals.article_generator_context.connect(setup_comments_count)
    signals.article_generator_write_article.connect(get_comments_count)
