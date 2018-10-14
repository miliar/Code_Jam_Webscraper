#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import izip
import sys

gooM = {
        ' ': ' ',
        'y': 'a',
        'e': 'o',
        'q': 'z',
}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def learn(ins, outs):
    if len(ins) != len(outs):
        raise ValueError, 'different lengths'
    for i, o in izip(ins, outs):
        if i in gooM and gooM[i] != o:
            raise Exception,  "Lie! {i} -> {fi}, {o}".format(i=i, fi=gooM[i], o=o)
        else:
            gooM[i] = o

def update():
    notkeys = [a for a in alphabet if a not in gooM]
    notvalues = [a for a in alphabet if a not in gooM.itervalues()]
    if len(notkeys) == len(notvalues) == 1:
        gooM[notkeys[0]] = notvalues[0]

def translate(s):
    return ''.join(gooM[c] for c in s)

learn('ejp mysljylc kd kxveddknmc re jsicpdrysi',  'our language is impossible to understand')
learn('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities')
learn('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up')

update()

if len(gooM) != len(alphabet) + 1:
    raise Exception, "Little learn :("
    
    
for i,line in enumerate(sys.stdin):
    if i == 0:
        continue
    print 'Case #{i}: {translation}'.format(i=i, translation=translate(line.strip()))
    