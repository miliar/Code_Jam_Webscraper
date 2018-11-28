#! /usr/bin/env python

import string

m = {}
m['y'] = 'a'
m['e'] = 'o'
m['q'] = 'z'


def add(e,g):
    for i in range(len(e)):
        m[g[i]] = e[i]
       
def trans(g):
    e = ''
    for i in range(len(g)):
        e = e + m[g[i]]
    return e

add('our language is impossible to understand', 'ejp mysljylc kd kxveddknmc re jsicpdrysi')
add('there are twenty six factorial possibilities','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
add('so it is okay if you want to just give up','de kr kd eoya kw aej tysr re ujdr lkgc jv')

gleft = string.ascii_lowercase
eleft = string.ascii_lowercase

for i in m:
    if i == ' ':
        continue
    gleft = gleft[:gleft.find(i)]+gleft[gleft.find(i)+1:]
    eleft = eleft[:eleft.find(m[i])]+eleft[eleft.find(m[i])+1:]
    
add(eleft, gleft)

n = input()
for i in range(n):
    s = raw_input()
    print 'Case #' + str(i+1) + ': ' + trans(s)
