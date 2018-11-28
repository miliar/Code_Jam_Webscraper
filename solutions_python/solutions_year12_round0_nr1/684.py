#!/usr/bin/python
import re
import sys
import io
import string
def ok(code,clear):
    assert len(code) == len(clear)
    return {a:b for (a,b) in zip(code,clear)}
test=(
('ejp mysljylc kd kxveddknmc re jsicpdrysi','our language is impossible to understand'),
('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','there are twenty six factorial possibilities'),
('de kr kd eoya kw aej tysr re ujdr lkgc jv','so it is okay if you want to just give up'))
def t(d,a):
    tr=string.maketrans(''.join(d.keys()),''.join(d.values()))
    return a.translate(tr)
d={}
for (a,b) in test:
    d.update(ok(a,b))
d['z']='q'
d['q']='z'
for (a,b) in test:
    assert t(d,a)==b
for (i,s) in enumerate(sys.stdin.readlines()):
    print('Case #{}: {}'.format(i,t(d,s.strip())))
