from operator import itemgetter
from math import pi

fin = open('A-large.in')
fout = open('A_out.txt', 'w')
T = int(fin.readline().split()[0])
print(T)

for i in range(T):
    dataIn = fin.readline().split()
    N = int(dataIn[0])
    K = int(dataIn[1])
    RH = list()
    for h in range(N):
        dataIn = fin.readline().split()
        RH.append([int(dataIn[0]), int(dataIn[1])])
        RH[h].append(RH[h][0] * RH[h][1])
    RS = sorted(RH, key = itemgetter(0), reverse = True)
    best = 0;
    for p in range(0, N - K + 1):
        rh = RS[p]
        res = 0
        RHAS = sorted(RS[p + 1 : N], key = itemgetter(2),
                      reverse = True)
        for pp in range(0, K - 1):
            res = res + RHAS[pp][2]
        res = res * 2 + rh[0] * rh[0] + rh[2] * 2
        if res > best:
            best = res
    fout.write('Case #' + str(i + 1) + ': ' + str(best * pi)
               + '\n')
        
fin.close()
fout.close()
