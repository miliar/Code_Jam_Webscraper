import sys
from collections import Counter
from copy import deepcopy

temp = sys.stdout
sys.stdout = open(r'C:\Users\palzle\Desktop\o.txt', 'w')

Q = open(r'C:\Users\palzle\Desktop\t.txt')
T = int(Q.readline())


def sol(d, n, ks, ss):
    res = 0
    for k, s in zip(ks, ss):
        cur = (d - k) / s
        res = max(res, cur)

    return d / res


for w in range(T):
    print('Case #%r:' % (w + 1), end=' ')
    d, n = map(int, Q.readline().split())
    ks, ss = [], []
    for _ in range(n):
        k, s = map(int, Q.readline().split())
        ks.append(k)
        ss.append(s)
    # print(d, n, ks, ss)
    res = sol(d, n, ks, ss)
    print(res)

sys.stdout = temp
