E = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

D = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""
import string

dic = {}
present = {}
for e, d in zip(E,D):
    if dic.has_key(e):
        assert dic[e] == d
    dic[e] = d
    present[d] = True

for l in string.ascii_lowercase:
    if not present.has_key(l):
        print l

dic['q'] = 'z'
dic['z'] = 'q'
# print dic

import sys 
rl = lambda : sys.stdin.readline().strip()
ncase = int( rl() )

for caseno in xrange( 1, ncase+1 ):
    inp = rl()
    ret = ''
    for l in inp:
        ret += dic[l]
    print "Case #%d: %s" % ( caseno, ret )
