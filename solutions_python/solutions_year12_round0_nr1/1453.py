import psyco
psyco.full()
import sys

import itertools


sg = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

s = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up""" 

alphas = 'abcdefghijklmnopqrstuvwxyz'

tran = {}
tran['q'] = 'z'
for i in xrange(len(sg)):
    if not sg[i] in ('\n', ' '):
        tran[sg[i]] = s[i]
for a in alphas:
    if a not in tran.values():
        tran['z'] = a  

#for cg,c in sorted(tran.items(), key=lambda a: a[0]):
#    print "%s --> %s" % (cg,c)

def calc(inp):
    out = ''
    for c in inp:
        if c != ' ':
            out += tran[c]
        else:
            out += c
    return out

def inGen():
    for line in open(sys.argv[1], 'r'):
        yield line.strip('\n')

ig = inGen()
ig.next()
cn = 1
for line in ig:
    v = calc(line)
    print "Case #%d: %s" % (cn,v)
    cn += 1


