'''
abeakkas
Google CodeJam 2017 - Round 1C
Problem B
 '''
# Python candir
import sys
import math

fin = open(sys.argv[1], 'r')
fout =  open(sys.argv[2], 'w')

T = int(fin.readline())

for iT in range(1, T + 1):
    l = fin.readline().split()
    Ac = int(l[0])
    Aj = int(l[1])
    acts = []
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(Ac):
        l = fin.readline().split()
        s = int(l[0])
        e = int(l[1])
        t1 += e - s
        acts.append((s, e, 1))
    for i in range(Aj):
        l = fin.readline().split()
        s = int(l[0])
        e = int(l[1])
        t2 += e - s
        acts.append((s, e, 2))
    n = 0
    acts.sort()
    pers1 = []
    pers2 = []
    print(acts)
    if acts[0][2] == 1:
        pers2.append(acts[0][0])
        t1 += acts[0][0]
    else:
        pers1.append(acts[0][0])
        t2 += acts[0][0]

    if acts[-1][2] == 1:
        pers2.append(1440 - acts[-1][1])
        t1 += 1440 - acts[-1][1]
    else:
        pers1.append(1440 - acts[-1][1])
        t2 += 1440 - acts[-1][1]

    if acts[0][2] != acts[-1][2]:
        n += 1
        t3 += 1440 + acts[0][0] - acts[-1][1]
    else:
        if acts[0][2] == 1:
            pers2.append(1440 + acts[0][0] - acts[-1][1])
            t1 += 1440 + acts[0][0] - acts[-1][1]
        else:
            pers1.append(1440 + acts[0][0] - acts[-1][1])
            t2 += 1440 + acts[0][0] - acts[-1][1]

    for i in range(len(acts) - 1):
        if acts[i][2] != acts[i + 1][2]:
            n += 1
            t3 += acts[i + 1][0] - acts[i][1]
        else:
            if acts[i][2] == 1:
                pers2.append(acts[i + 1][0] - acts[i][1])
                t1 += acts[i + 1][0] - acts[i][1]
            else:
                pers1.append(acts[i + 1][0] - acts[i][1])
                t2 += acts[i + 1][0] - acts[i][1]

    print("{} {} {} {}".format(iT, t1, t2, t3))
    if t1 + t3 < 720:
        t = t1 + t3
        pers1.sort()
        while t < 720:
            t += pers1.pop()
            n += 2
    if t2 + t3 < 720:
        t = t2 + t3
        pers2.sort()
        while t < 720:
            t += pers2.pop()
            n += 2
    print("Case #{}: {}".format(iT, n), file=fout)
