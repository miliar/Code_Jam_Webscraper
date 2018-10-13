def calc(t, s):
    x = t[:]
    for i in xrange((len(x) - 1) // 2 - 1, -1, -1):
        j = 2 * i + 1
        k = j + 1
        if i in s: x[i] = 5 - x[i]
        if x[i] == 2:
            x[i] = 1 if x[j] or x[k] else 0
        else:
            assert x[i] == 3
            x[i] = 1 if x[j] and x[k] else 0
    return x[0]

def solve(t, c, V):
    BIG = 10**100
    min_s = BIG
    for b in xrange(2**(len(c))):
        s = set()
        i = 0
        while b > 0:
            if b % 2: s.add(c[i])
            b //= 2
            i += 1
        # s is a set of nodes that we will change
        if V == calc(t, s): min_s = min(min_s, len(s))
    if min_s == BIG:
        return "IMPOSSIBLE"
    return str(min_s) 

for n in range(input()):
    M, V = map(int, raw_input().split())
    t, c = [], []
    for i in xrange((M - 1) // 2):
        G, C = map(int, raw_input().split())
        t.append(G + 2)
        if C: c.append(i)
    for i in xrange((M + 1) // 2):
        t.append(input())
    print("Case #%d: %s" %(n + 1, solve(t, c, V)))