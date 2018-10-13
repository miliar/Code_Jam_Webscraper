__author__ = 'janux'


from decimal import Decimal
from collections import namedtuple

State = namedtuple('State', ['time', 'cookies', 'production'])


T = int(raw_input())

result = Decimal(1000.0)

def f(time, cookies, production, X, C, F):
    global result
    print time, cookies, production, result
    if cookies >= X:
        result = min(result, time)
    else:
        if time > result:
            return result
        direct = f(time + (X - cookies) / production, X, production, X, C, F)
        if C > cookies:
            if (time + (C - cookies) / production) + (X / (production + F)) > result:
                return result
            farm = f(time + (C - cookies) / production, 0, production + F, X, C, F)
        else:
            n, r = divmod(C, cookies)
            farm = f(time, cookies - n * C, production + n * F, X, C, F)
            #for i in range(n):
            if r > 0:
                left = (cookies - n * C)
                farm = min(farm, f(time + (C - left) / production, 0, production + (n + 1) * F, X, C, F))
        return min(direct, farm)


def greedy(C, F, X):
    time = Decimal(X / Decimal(2.0))
    p = Decimal(2.0)
    tt = C / p
    while True:
        p += F
        if tt + (X / p) >= time:
            break
        time = tt + (X / p)
        tt += C / p
    return time




for test in range(0, T):
    args = raw_input().split()
    C, F, X = Decimal(args[0]), Decimal(args[1]), Decimal(args[2])
    print 'Case #%d: %s' % ((test + 1), str(greedy(C, F, X)))

