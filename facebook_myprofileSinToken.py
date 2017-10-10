# -*- coding: utf-8 -*-
"""
Editor de Spyder
Autor: dkl182
Este es un archivo temporal
"""

import os
import json
import facebook
import csv
import requests

if __name__ == '__main__':
    token = ""
    
    graph = facebook.GraphAPI(token)
    all_fields = [
            'message',
            '',
            '',
            '',
            '',
            '',
            ''
            ]
    all_fields = ','.join(all_fields)
    posts = graph.get_connections('me', 'posts')
    
    while True:
        try:
            with open('my_posts_json2','a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                    
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break
