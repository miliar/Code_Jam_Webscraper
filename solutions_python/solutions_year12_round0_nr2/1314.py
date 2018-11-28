import sys

T = int(sys.stdin.readline())
for i in range(T):
    t = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    N = t.pop(0)
    S = t.pop(0)
    p = t.pop(0)
    n = 0
    assert len(t) == N
    for g in t:
        if (g / 3) + min(1, g % 3) >= p:
            n += 1
        elif S and p >= 2 and (p - 2) * 3 in (g - 2, g - 3, g - 4):
            n += 1
            S -= 1
    print "Case #%d: %d" % (i+1, n)

