# https://code.google.com/codejam/contest/1460488/dashboard#s=p0
from sys import stdin as i

a = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'

b = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

mymap = dict(zip(a,b))
mymap['z'] = 'q'
mymap['q'] = 'z'

for j in range(int(i.readline())):
    print "Case #%d: %s" % ((j+1), ''.join([mymap[c] for c in i.readline().strip()]))
