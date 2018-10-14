import sys

t = int(sys.stdin.readline().strip())

for c in range(t):
    s_max, digits = tuple(x.strip() for x in sys.stdin.readline().strip().split())
    res = 0
    tot = 0
    for i, v in enumerate(list(int(x) for x in digits)):
        if tot < i:
            res += 1
            tot += 1
        tot += v
    print("Case #%d: %d" % (c+1, res))
