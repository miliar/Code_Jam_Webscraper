import sys
import numpy as N

def pal(i):
    i = str(i)
    return i == i[::-1]

data = open(sys.argv[1]).read().splitlines()[1:]
for n,d in enumerate(data):
    a,b = map(int, d.split())
    x = N.arange(a,b+1)
    w = N.sqrt(x) == N.sqrt(x).astype('int')
    x = x[w].astype('int')
    out = N.array(map(pal, x)).astype('bool') & \
          N.array(map(pal, N.sqrt(x).astype('int'))).astype('bool')
    print 'Case #%i: %i' % (n+1, out.nonzero()[0].shape[0])
