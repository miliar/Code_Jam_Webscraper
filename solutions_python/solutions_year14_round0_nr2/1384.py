
def rpoly(a, y):
    return y / a


def fun():
    C, F, X = (float(i) for i in raw_input().split(' '))
    a = 2.0
    t = rpoly(a, X)
    cx = rpoly(a, C)
    a += F

    while True:
        prev = t
        t = rpoly(a, X) + cx
        if prev < t:
            return prev
        else:
            cx += rpoly(a, C)
            a += F


T = int(raw_input())
for t in range(1, T + 1):
    print "Case #{}: {}".format(t, fun())
