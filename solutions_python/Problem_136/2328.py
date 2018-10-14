#!/usr/bin/python
for i in range(int(input())):
    C, F, X = map(float, input().split())
    pro = 2.
    res = 0.
    while 1:
        a = X / pro
        b = C / pro + X / (pro + F)
        if a < b:
            res += a
            break
        else:
            res += C / pro
            pro += F
    print('Case #{0}: {1:.7f}'.format(i+1, res))
