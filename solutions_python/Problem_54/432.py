d = open("b.in", "r").read().split()
p = 0

def gcd(a,b):
    while a and b:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b

def next():
    global d, p
    p += 1
    return int(d[p-1])

of = open("b.out", "w")
t = next()
for i in xrange(t):
    n = next()
    o = []
    for j in xrange(n):
        o.append(next())
    
    o = list(set(o))
    o.sort()
    nok = reduce(gcd, map(lambda a, b: b-a, o[:-1], o[1:]))

    r = (nok - (o[0] % nok)) % nok
    of.write("Case #%d: %d\n" % (i+1, r))
of.close()
