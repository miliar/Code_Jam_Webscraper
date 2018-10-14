import math

import itertools

PI =  3.1415926535897932384626433832795028841971693993751058209749445923078164062862089
def computeArea(radi, high, cnt = False):
    if cnt:
        return 2*radi*high + radi**2
    else:
        return 2 * PI * radi * high

def cal(radi, high):
    return 2 * radi * high
def max_element(val,f):
    l = [(b,a) for (a,b) in val]
    l.sort(reverse=True)

    r = l[:f]

    if len(r) ==f:
        return sum([cal(a[0], a[1]) for b,a in r])
    else:return -1

def process(n, f):
    val = []
    for x in range(n):
        k = [int(x) for x in input().split()]
        val.append(k)

    val.sort(reverse=True)
    q = []

    for x in val:
        q.append((x, cal(x[0], x[1])))
    # for x in q:
    #     print(x)
    w =[]
    for x in range(len(q)):
        a , b = q[x]
        # print(q[x])
        s = computeArea(a[0], a[1], True)
        er = q[x+1:]
        s+=max_element(er,f-1)
        w.append(s*PI)

    w.sort(reverse=True)
    return w[0]
    # print(w[0])




t = int(input())

for x in range(t):
    n, k =[int(x) for x in input().split()]
    # print(n, k)
    ty = process(n, k)
    # print(computeArea(100, 20))
    s = 'Case #{0}: '.format(x+1)
    # print(ty)
    print(s+ str(round(ty,9)))