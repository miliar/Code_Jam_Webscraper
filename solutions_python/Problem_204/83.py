import sys, math
import numpy as np

INPUT_NAME = sys.argv[1]
OUTPUT_NAME = INPUT_NAME.split(".")[0] + ".out"

f = open(INPUT_NAME,'r')
out = open(OUTPUT_NAME,'w')

num_cases = int(f.readline().strip())

for test in range(num_cases):
    n,p = tuple(map(int,f.readline().strip().split(" ")))
    R = list(map(int,f.readline().strip().split(" ")))
    Q = [list(map(int,f.readline().strip().split(" "))) for i in range(n)]
    Q2 = [[] for i in range(n)]
    for i in range(n):
        for j in range(p):
            Q[i][j] = 1.0*Q[i][j] / R[i]
            qij = []
            for k in range(max(1,int(math.floor(0.8*Q[i][j]))),int(math.ceil(1.2*Q[i][j])+1)):
                if Q[i][j] >= 0.9*k and Q[i][j] <= 1.1*k:
                    qij.append(k)
            if qij != []:
                Q2[i].append((qij[0],qij[len(qij)-1]))
        Q2[i] = sorted(Q2[i], key=lambda x: (x[1], x[0]))

    Q2[0] = sorted(Q2[0], key=lambda x: (x[0], x[1]))
    ans = 0
    i = 0
    while i < len(Q2[0]):
        to_remove = [-1 for ii in range(n)]
        to_remove[0] = i
        valid = True
        for j in range(1,n):
            for k in range(len(Q2[j])):
                if Q2[j][k][0] <= Q2[0][i][1] and Q2[j][k][1] >= Q2[0][i][0]:
                    to_remove[j] = k
                    break
            if to_remove[j] == -1:
                valid = False
                break
        if valid:
            for j in range(n):
                Q2[j].pop(to_remove[j])
            ans += 1
        else:
            i += 1

    out.write("Case #%d: %d\n" % (test+1, ans))
