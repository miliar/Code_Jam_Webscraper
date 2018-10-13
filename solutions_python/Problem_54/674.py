#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import cgi
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from time import sleep, clock

import copy

def gcd_2(u, v):
    return gcd_2(v, u % v) if v else abs(u)

def gcd(l):
    if len(l) is 1: return l[0]
    sl = copy.copy(l)
    zlist = []
    for i in l:
        del sl[0]
        for j in sl:
            zlist.append(gcd_2(i,j))

    return min(zlist)

def solver(line):
    line.reverse()
    N = line.pop()

    zlist = []
    sline = copy.copy(line)
    for i in line:
        del sline[0]
        for j in sline:
            zlist.append(abs(i-j))

    T = gcd(zlist)

    if line[0] % T is 0: return 0
    #solution = str([T - line[0] % T,T])
    solution = str(T - (line[0] % T))
    return solution

def jamit(it):
    it = it.split("\r\n")
    it.reverse()
    total_cases = int(it.pop())
    t_range = range(1,total_cases+1)
    olist = range(1,total_cases+2)

    for case_number in t_range:
        line = map(int,it.pop().strip().split(' '))
        olist[case_number] = solver(line)

    out = ""
    for c in t_range:
        out += "Case #" + str(c) + ": " + str(olist[c])+"<br />"

    return out

class MainHandler(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'code-jam.html')
        self.response.out.write(template.render(path,None))

    def post(self):
        rel_input = cgi.escape(self.request.get('input-area'))

        clock()
        rel_vars = {"output"  :jamit(rel_input),
                    "clock"   :clock()}

        path = os.path.join(os.path.dirname(__file__), 'code-jam.html')
        self.response.out.write(template.render(path,rel_vars))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
