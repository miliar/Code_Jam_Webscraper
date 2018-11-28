from collections import defaultdict

for t in range(int(raw_input())):
    l = []
    co = {}
    op = defaultdict(set)
    raw = raw_input().split()
    deny = set()
    for i in range(int(raw.pop(0))):
        w = raw.pop(0)
        co[w[0],w[1]] = w[2]
        co[w[1],w[0]] = w[2]

    for i in range(int(raw.pop(0))):
        w = raw.pop(0)
        op[w[0]].add(w[1])
        op[w[1]].add(w[0])

    a = None
    for b in raw.pop():
        if a:
            p = (a,b)
            if p in co:
                l.append(co[p])
                a = None
                continue
            l.append(a)
            deny.update(op[a])

        a = b
        if a in deny:
            l = []
            deny.clear()
            a = None

    if a:
        l.append(a)

    print 'Case #%d: [%s]' % (t+1, ", ".join(l))

