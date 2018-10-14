import math
def get_key(item):
    return item[0]
def power(c):
    if len(c) == 0:
        return [[]]
    r = power(c[:-1])
    return r + [s + [c[-1]] for s in r]
def comb(c, n):
    return [s for s in power(c) if len(s) == n]
def area(p):
    res = (0)
    for i in range(len(p)):
        res += float(2*p[i][0]*p[i][1])
        if i>0:
            res += (pow(p[i][0],2)-pow(p[i-1][0],2))
        else:
            res += (pow(p[i][0],2))
    res *= (math.pi)
    return float(res)
tc = int(input())
for i in range(1, tc + 1):
    print("Case #%d: " % i, end='')
    n, k = map(int, input().split())
    # print('N: {}, K: {}'.format(n,k))
    p = []
    for j in range(1, n + 1):
        r, h = map(int, input().split())
        # print('P{} -> R: {}, H: {}'.format(j,r,h))
        p.append([r,h])
    p = sorted(p, key=get_key)
    p = comb(p,k)
    x = -1
    for j in p:
        y = area(j)
        if x < y:
            x = y
    print(x)