a = ' abcdefghijklmnopqrstuvwxyz'
b = ' ynficwlbkuomxsevzpdrjgthaq'
d = dict(zip(b,a))

def solve():
    s = raw_input()
    return "".join([d[c] for c in s])

t = input()
for i in xrange(t):
    print "Case #%d: %s"%(i+1,solve())
