class sstr(str):
    def __repr__(self): return self

from collections import defaultdict
for trial in range(int(raw_input())):
    L = []
    C = {}
    O = defaultdict(set)
    raw = raw_input().split()
    for i in range(int(raw.pop(0))):
        c = raw.pop(0)
        C[c[0],c[1]] = c[2]
        C[c[1],c[0]] = c[2]

    for i in range(int(raw.pop(0))):
        c = raw.pop(0)
        O[c[0]].add(c[1])
        O[c[1]].add(c[0])

    def add(c):
        L.append(c)
        p = tuple(L[-2:])
        if p in C:
            L[-2:]=[]
            return add(C[p])

        for i in O[c]:
            if i in L:
                L[:]=[]
                break
        # print L

    map(add,raw.pop())

    print 'Case #%d: %r' % (trial+1, map(sstr,L))