import re

t1="""ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""

t2="""our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

d = dict(zip(t1, t2))
d['y']='a'
d['e']='o'
d['q']='z'
d['z']='q'
d.pop('\n')
letters = 'abcdefghijklmnopqrstuvwxyz'

f = open('input1.txt')
f.readline()
for idx, l in enumerate(f):
    l = l.strip()
    s = ''.join(d[x] for x in l)
    print 'Case #%d: %s' % (idx + 1, s)
