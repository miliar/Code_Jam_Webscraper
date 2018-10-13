#!/usr/bin/python
import sys
from string import maketrans

myStrip = lambda x: x.translate(None,' \n') 

orig = myStrip('''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
''')
res = myStrip('''
              our language is impossible to understand
              there are twenty six factorial possibilities
              so it is okay if you want to just give up
                ''')

transDict = {}
for o,r in zip(orig,res):
    if o in transDict and transDict[o] != r: raise('translation error')
    transDict[o]=r

transDict['q'] = 'z'
transDict['z'] = 'q'

T = int(sys.stdin.readline())
for i in xrange(T):
    l = sys.stdin.readline()
    l = l.translate(maketrans(str(transDict.keys()),str(transDict.values())))
    print 'Case #%d: %s' % (i+1,l.strip())
