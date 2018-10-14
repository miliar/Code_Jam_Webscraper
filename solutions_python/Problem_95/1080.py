#!/usr/bin/python

from sys import stdin

s1 = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvqz
"""

s2 = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upzq
"""


from itertools import *


x = dict(izip(s1, s2))


n = int(stdin.readline())

for i in xrange(1, n + 1):
    l = stdin.readline()[:-1]
    print "Case #%d: %s" % (i, "".join(imap(lambda c: x[c], l)))

