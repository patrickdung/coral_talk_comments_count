Pelican plugin for getting the comments count of an article
-----------------------------------------------------------

This plugin references several Pelican plugins.
So this plugin would be in AGPLv3 license.

- [Pelican Plugins](https://github.com/getpelican/pelican-plugins/)

Parameters to be added in order to use this plugin
--------------------------------------------------

Parameters are: CORAL_DOMAIN_NAME, CORAL_STATIC_COMMENTS_COUNT

- CORAL_DOMAIN_NAME = "<input your domain name of Coral Talk server'
- CORAL_STATIC_COMMENTS_COUNT = True

How to use it in the template
-----------------------------

```
    {% if CORAL_STATIC_COMMENTS_COUNT and 'coral_talk_comments_count' in PLUGINS %}
      Comments: {{article.coral_comments.count}}
    {% endif %}
```

License
-------
Unless the folder itself contains a LICENSE stating otherwise, all the files
distributed here are released under the GNU AFFERO GENERAL PUBLIC LICENSE.
