from operator import mul
from functools import reduce


def solve():
    n, k = map(int, input().split())
    u = float(input())
    prob = list(map(float, input().split()))
    prob.sort()
    prob.append(1.0)

    last = prob[0]
    i = 0
    while i <= n:
        while i < n and prob[i] <= last:
            i += 1
        target = min(prob[i], u / i + last)
        #print('u=',u, 'i=', i, 'last=', last, 'target=', target)
        for j in range(i):
            prob[j] = target
        u -= (target - last) * i
        last = target
        if abs(u) <= 1e-06:
            break
    return reduce(mul, prob, 1.0)


for t in range(int(input())):
    print('Case #%d: %r' % (t + 1, solve()))
