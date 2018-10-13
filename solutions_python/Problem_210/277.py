from __future__ import print_function
s = """5
1 1
540 600
840 900
2 0
900 1260
180 540
1 1
1439 1440
0 1
2 2
0 1
1439 1440
1438 1439
1 2
3 4
0 10
1420 1440
90 100
550 600
900 950
100 150
1050 1400
"""
s = open('B-small-attempt0.in').read()
# s = open('B-large.in').read()
"""
"""
import sys
import math

ss = s.split('\n')
T = int(ss[0])

f = open('B.out', 'w')
# f = sys.stdout

idx = 1
for t in range(0, T):
    Ac, Aj = [int(x) for x in ss[idx].split(' ')]
    idx += 1
    Cs = []
    C_t = 0
    J_t = 0
    for c in range(Ac):
        Cc, Dc = [int(x) for x in ss[idx].split(' ')]
        idx += 1
        Cs.append(['c', Cc, Dc, Dc - Cc])
        C_t += Dc - Cc
    for j in range(Aj):
        Cj, Dj = [int(x) for x in ss[idx].split(' ')]
        idx += 1
        Cs.append(['j', Cj, Dj, Dj - Cj])
        J_t += Dj - Cj
    Cs = sorted(Cs, key=lambda x:x[1])
    trans = Cs[0][1]
    # print(trans)
    for c in Cs:
        c[1] -= trans
        c[2] -= trans
    # print(Cs)
    gaps = []
    for i in range(len(Cs)):
        r = Cs[i]
        l = Cs[i - 1]
        # print(l, r)
        cls = r[0] == l[0]
        sym = None
        if cls:
            sym = r[0]
        if i == 0:
            gaps.append([cls, l[2], r[1], 1440 - l[2], sym])
        else:
            gaps.append([cls, l[2], r[1], r[1] - l[2], sym])
    # print(gaps)
    swap_cnt = 0
    gap_same = []
    for g in gaps:
        if g[0] == False:
            swap_cnt += 1
        else:
            gap_same.append(g)
    gap_same = sorted(gap_same, key=lambda x: x[3])
    # print(gap_same)
    flag = False
    for g in gap_same:
        if flag:
            swap_cnt += 2
        elif g[4] == 'c':
            C_t += g[3]
            if C_t > 720:
                swap_cnt += 2
                flag = True
        elif g[4] == 'j':
            J_t += g[3]
            if J_t > 720:
                swap_cnt += 2
                flag = True
    # print(swap_cnt)
    print('Case #%d: %d'%(t+1, swap_cnt), file=f)