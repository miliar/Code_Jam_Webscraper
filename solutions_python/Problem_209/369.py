from __future__ import print_function
s = """4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4
"""
# s = open('A-small-attempt5.in').read()
s = open('A-large.in').read()
"""Case #1: 138230.076757951
Case #2: 150796.447372310
Case #3: 43982.297150257
Case #4: 625.176938064
"""
import sys
import math

ss = s.split('\n')
T = int(ss[0])

f = open('A.out', 'w')
# f = sys.stdout

idx = 1
for j in range(0, T):
    N, K = [int(x) for x in ss[idx].split(' ')]
    idx += 1
    Ps = []
    Rs = {}
    for n in range(N):
        Ri, Hi = [int(x) for x in ss[idx].split(' ')]
        idx += 1
        Side = 2.0*Ri*Hi
        if not Rs.has_key(Ri):
            Rs[Ri] = []
        Rs[Ri].append([n,Ri,Hi,Side])
    Rs_key_sorted = sorted(Rs.keys(), reverse=True)
    for Rs_key in Rs_key_sorted:
        arr = Rs[Rs_key]
        arr = sorted(arr, key=lambda x: x[3], reverse=True)
        for x in arr:
            Ps.append(x)
    best = 0.0
    best2 = 0.0
    for n in range(N-K+1):
        SubP = Ps[n+1:]
        Ss = sorted(Ps, key=lambda x: x[3], reverse=True)
        Ss2 = sorted(SubP, key=lambda x: x[3], reverse=True)
        Total = 0.0
        Total2 = 0.0
        r = Ps[n][1]
        area = r*r
        Total += area
        Total += Ps[n][3]
        Total2 = Total
        for l in range(K-1):
            # Total += Ss[l][3]
            Total2 += Ss2[l][3]
        if Total2 > best2:
            # best = Total
            best2 = Total2
    # print(N, K, R, H, Ps)
    # print(best, best2, best==best2)
    print('Case #%d: %.08f'%(j+1, best2*math.pi), file=f)