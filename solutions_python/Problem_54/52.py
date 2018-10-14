import sys
rl = lambda: sys.stdin.readline().strip()

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

cases = int(rl())
for cc in range(cases):
    t = map(int, rl().split())[1:]
    t.sort()

    deltas = [a-b for a, b in zip(t[1:], t)]
    z = reduce(gcd, deltas)
    sol = max(z - (v % z) if v % z > 0 else 0 for v in t)

    print "Case #%d: %d" % (cc+1, sol)


