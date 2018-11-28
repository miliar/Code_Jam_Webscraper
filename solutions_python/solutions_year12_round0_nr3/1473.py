from itertools import combinations

def recycled_pairs(n,b,a):
    c = 0
    ns = []
    for _ in range(len(n)):
        if n[0] != '0' and n not in ns:
            ns.append(n)
        n = n[1:] + n[0]
    ns = [int(x) for x in ns]
    pairs = [x for x in combinations(ns,2) if x[0] != x[1]]
    for pair in pairs:
        s.add(pair[0])
        s.add(pair[1])
        if max(pair) <= b and min(pair) >= a:
            c += 1
    return c

with open("output3.txt",'w') as out:
    with open("input3.txt") as f:
        t = int(f.readline().strip())
        for x in range(1,t+1):
            s = set()
            a,b = [int(i) for i in f.readline().strip().split()]
            p = 0
            for n in range(a,b):
                if n not in s:
                    p += recycled_pairs(str(n),b,a)
            out.write("Case #%d: %d\n" % (x,p))
