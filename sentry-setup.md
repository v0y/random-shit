```bash
sudo easy_install -U sentry
sentry init
vim ~/.sentry/sentry.conf.py
sentry upgrade
sentry start
sentry createuser
gnome-open http://127.0.0.1:9000
```

```python
# ~/.sentry/sentry.conf.py

SENTRY_URL_PREFIX = 'http://127.0.0.1:9000'                                      
SENTRY_CACHE = 'sentry.cache.django.DjangoCache'                                 
SENTRY_ADMIN_EMAIL = 'a@a.pl'                                                    
SENTRY_WEB_PORT = 9000
```
