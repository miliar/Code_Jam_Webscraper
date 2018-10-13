'''
 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'

ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand

rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up

'''
from string import maketrans

english = 'abcdefghijklmnopqrstuvwxyz'
googlerese = 'ynficwlbkuomxsevzpdrjgthaq'

from sys import stdin

n = int(stdin.readline())

for i in range(1,n+1):
    line = stdin.readline()
    translated = line.strip().translate(maketrans(googlerese, english))
    print 'Case #%s: %s' % (i, translated)