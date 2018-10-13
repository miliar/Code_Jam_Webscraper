def bla1(a,b):
    a.sort()
    b.sort()
    for i in xrange(len(a)):
        if all(x>y for x,y in zip(a[i:],b)):
            return len(a)-i
    return 0

def bla2(a,_b):
    B = 0
    b = _b[::]
    for x in a:
        try:
            c = min(f for f in b if f > x)
        except:
            c = min(b)
            B += 1
        b.remove(c)
    return B

def bla(a,b):
    return bla1(a,b),bla2(a,b)

f = map(str.strip,open('D-large.in'))

case = 1
i = 1
while i < len(f):
    n = int(f[i])
    a = map(float,f[i+1].split())
    b = map(float,f[i+2].split())
    i += 3
    print 'Case #%d: %d %d'%((case,)+bla(a,b))
    case += 1
