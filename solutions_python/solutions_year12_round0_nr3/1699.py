def recycles(n, m):
    x = toList(n)
    l = []
    for i in range(1, len(x)):
        recycle = toInt(x[i:] + x[0:i])
        if recycle > n and recycle < m:
            l.append(recycle)
    return l

def toList(value):
    digits = []
    while value: value,b = divmod(value,10); digits.insert(0,b)
    return digits

def toInt(l):
    return int(''.join(map(str, l)))


def case(x,y):
    s = set()
    for n in range(x,y):
        for r in recycles(n, y+1):
            s.add((n,r))
    return len(s)

t = int(raw_input())
i = 0
while i < t:
    i += 1
    x,y = [int(x) for x in raw_input().split()]
    print "Case #%d: %d" % (i, case(x,y))
