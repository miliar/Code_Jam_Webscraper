T = int(raw_input())

def inc(x, y, m):
    if x < 0:
        return
    if x not in d:
        d[x] = 0
        e[x] = 0
        f[x] = 0
        a.append(x)
    d[x] = d[x] + y
    if m == 0:
        e[x] = e[x] + y
    else:
        f[x] = f[x] + y

def get(v):
    s = 0
    for it in v:
        s += it[1]
        if s >= k:
            return str(it[0])
    return ""

for t in range(T):
    n, k = map(int, raw_input().split(" "))
    d = {}
    e = {}
    f = {}
    a = []
    b = []
    c = []
    d[n] = 1
    a.append(n)
    while len(a) != 0:
        a.sort()
        x = a.pop()
        y = d[x]
        x -= 1
        inc(x / 2, y, 0)
        inc((x + 1) / 2, y, 1)
    del d[n]
    keys = e.keys()
    keys.sort()
    for x in keys:
        b.append((x, e[x]))
    keys = f.keys()
    keys.sort()
    for x in keys:
        c.append((x, f[x]))
    b.reverse()
    c.reverse()
    print "Case #" + str(t + 1) + ": " + get(c) + " " + get(b)
