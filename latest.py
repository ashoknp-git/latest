#!/usr/bin/env python
from fastcgi import *
from fastcore.script import *
from fastcore.utils import *
from fastcore.foundation import *
from warnings import warn
import sys,os

sock = '/var/run/caddy/fcgi.sock'
if os.path.exists(sock): os.unlink(sock)

@fastcgi(sock)
def run():
    print(f'Content-type: text/plain\n')
    try: _,user,repo = os.environ['PATH_INFO'].split('/')
    except ValueError:
        print('!!!Invalid path')
        return

    rels=L(urljson(f'https://api.github.com/repos/{user}/{repo}/releases/latest')['assets'])
    print('\n'.join(rels.itemgot('browser_download_url')))

