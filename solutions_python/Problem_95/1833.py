a = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""
b = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

d = {}
for p, q in zip(a,b):
  d[p] = q
d['q'] = 'z'
d['z'] = 'q'

with open('A-small.in') as f:
  n = int(f.readline().strip())
  for i in xrange(0, n):
    line = f.readline().strip()
    g = ''.join([d[p] for p in line])
    print 'Case #{}: {}'.format(i+1, g)
