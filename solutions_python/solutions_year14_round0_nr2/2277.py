from __future__ import print_function
from __future__ import division

T = int(input())
for i in range(T):
    C, F, X = map(float, input().split(' '))
    t = 0
    n = 0
    r = 2
    while n < X:
        if (X - n) < C:
            t += (X - n)/r
            n = X
            break
        else:
            t += C/r
            n = n + C
            if (X - n)/r > (X - n + C)/(r + F):
                # print("brought cookie: {t}, {n}, {r}".format(t=t, n=n, r=r))
                r += F
                n = n - C
    print("Case #{n}: {time}".format(n=i+1, time=t))
