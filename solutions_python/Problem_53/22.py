import sys
rl = lambda: sys.stdin.readline().strip()

t = int(rl())
for cc in range(t):
    n, k = map(int, rl().split())
    print "Case #%d: %s" % (cc+1, "ON" if (k+1) % (2**n) == 0 else "OFF")

