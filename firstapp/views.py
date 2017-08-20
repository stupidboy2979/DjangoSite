# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from firstapp.models import People
from django.shortcuts import render,HttpResponse
from django.template import Context, Template

# Create your views here.
def first_try(request):
    person = People(name='Spock',job='officer')
    html_string = '''
    <html>
      <head>
        <meta charset="utf-8">
        <title></title>
      </head>
      <body>
        <h1 class="ui center aligned icon header">
            <i class="hand spock icon"></i>
            Hello, {{person.name}}
      </body>
    </html>
    '''
    t = Template(html_string)
    c = Context({'person':person})
    web_page = t.render(c)
    return HttpResponse(web_page)
