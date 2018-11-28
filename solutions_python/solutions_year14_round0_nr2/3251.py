#!/bin/python
T = int(raw_input())

template = "Case #{}: {}"


def tern(func, l, r):
    #print("->", l, r)
    if r - l < 3:
        #print "TERN END", l, r, "->",  [func(j) for j in range(l, r+1)]
        #print min(enumerate([func(j) for j in range(l, r+1)], l), key=lambda x: x[1])[0]
        return min(enumerate([func(j) for j in range(l, r+1)], l), key=lambda x: x[1])[0]
    else:
        lT = (2*l + r)/3
        rT = (l + 2*r)/3
        #print(lT, rT)
        if func(lT) < func(rT):
            r = rT
        else:
            l = lT
        return tern(func, l, r)

for i in range(1, T+1):
    C, F, X = list(map(float, raw_input().split()))

    def cost(B):
        s = sum([1.0/(2.0 + j*F) for j in range(0, B)])
        res = C*s + X/(2.0 + B*F)
        #print "Cost", B, res
        return res

    max_B = int(X/C) + 1
    count = tern(cost, 0, max_B)
    print template.format(i, cost(count))