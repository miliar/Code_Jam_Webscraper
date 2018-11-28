
import math

# cookie/s
cps = 2

t = int(raw_input())
for case in range(0, t):
    (C, F, X) = map(float, raw_input().split(' '))

    def estimate(n):
        return C * sum(map(lambda i: 1.0 / (cps + i*F), range(0, n))) + X / (cps + n*F)
    def tsearch(l, r):
        while abs(l-r) > 2:
            lv = estimate(int((2*l + r) / 3))
            rv = estimate(int((l + 2*r) / 3))

            if(lv > rv):
                l = int((2*l + r) / 3)
            else:
                r = int((l + 2*r) / 3)
        return (l, r)

    maxn = int(math.ceil(max(X / float(C) - (cps + F) / float(F), 1)))
    (l, r) = tsearch(0, maxn)
    ans = min(map(estimate, range(l, r+1)))

    print("Case #%d: %.7f" % (case+1, ans))
