import sys

t = int(sys.stdin.readline())

def solve(x, s, r, t, n):
    sum = 0
    lens = []
    for i in range(n):
        b, e, w = map(int, sys.stdin.readline().split())
        lens.append((e-b, w+s))
        sum += e-b
    lens.append((x - sum, s))
    lens = sorted(lens, key=lambda x: x[1])
    sum = 0
    for (d, w) in lens:
        if t > 0:
            if (r - s + w) * t < d:
                dd = (r-s+w) * t
                sum += t
                sum += float(d - dd) / w
                t = 0
            else:
                tt = float(d) / (r-s+w)
                sum += tt
                t -= tt
        else:
            sum += float(d) / w
    print sum

for i in range(t):
    a = map(int, sys.stdin.readline().split())
    print "Case #%d:" % (i+1),
    solve(*a)
