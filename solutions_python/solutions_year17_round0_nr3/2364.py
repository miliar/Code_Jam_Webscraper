import fileinput
from collections import defaultdict

cases = [[int(x) for x in c.split()] for c in list(fileinput.input())[1:]]
for i, (n, k) in enumerate(cases):
    d, b, c, l, r = False, defaultdict(int), 1, 0, 0
    b[n] = 1
    while not d:
        for x in range(c):
            if k == 0:
                d = True
                break
            o = max(b.keys())
            l = o // 2
            r = o - l - 1
            b[l] += 1
            b[r] += 1
            b[o] -= 1
            k -= 1
            if b[o] == 0:
                del b[o]
        c *= 2
    print("Case #{}: {} {}".format(i + 1, max(l, r), min(l, r)))
