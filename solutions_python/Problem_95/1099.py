# -*- coding: utf-8 -*-
import sys


sin = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
       'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
       'de kr kd eoya kw aej tysr re ujdr lkgc jv']

sout = ['our language is impossible to understand',
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up']

maps = {}

for i in range( len(sin) ):
    for idx, val in enumerate( sin[i] ):
        maps[ val ] = sout[i][idx]

#print len(maps)
#print maps

maps['q'] = 'z'
maps['z'] = 'q'

#for i in [ chr(n) for n in range(ord('a'), ord('z')+1)]:
#   try:
#       print maps[i]
#   except:
#       print 'error: ', i


f = open(sys.argv[1], 'r')
line = f.readline().strip()

for idx in range( int(line) ):
    res = ''
    for j in f.readline().strip():
        res = res + maps[j]
    print "Case #%d: %s" % (idx+1, res)  
