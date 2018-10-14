#!/usr/bin/env python
tc = int(input())

def getTT(a, f, c, x, cps):
    if a == 0:
        return x/cps
    return ttB(a, c, f, cps) + x/(cps+a*f)

def ttB(a, c, f, cps):
    res = 0.0
    while a > 0:
        res += c/(cps+(a-1)*f)
        a = a-1
    return res

for t in range(tc):
    info = input().split()
    c = float(info[0])
    f = float(info[1])
    x = float(info[2])
    cps = 2.0

    a = 0
    actual = getTT(0, f, c, x, cps)
    while True:
        a = a+1
        prox = getTT(a, f, c, x, cps)
        if actual < prox:
            break
        actual = prox

    res = "%.7f" % actual
    print("Case #" + str(t+1) + ": " + res)