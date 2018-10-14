from operator import itemgetter

fin = open('B-large.in')
fout = open('B_out.txt', 'w')
T = int(fin.readline().split()[0])
print(T)

for i in range(T):
    dataIn = fin.readline().split()
    Ac = int(dataIn[0])
    Aj = int(dataIn[1])
    CJ = list()
    CT = 0
    JT = 0
    for a in range(Ac):
        dataIn = fin.readline().split()
        CJ.append([int(dataIn[0]), int(dataIn[1]), 'C'])
        CT = CT + CJ[a][1] - CJ[a][0]
    for a in range(Aj):
        dataIn = fin.readline().split()
        CJ.append([int(dataIn[0]), int(dataIn[1]), 'J'])
        JT = JT + CJ[a + Ac][1] - CJ[a + Ac][0]

    CJ = sorted(CJ, key = itemgetter(0))
    CJEX = CJ + [list(CJ[0])]
    CJEX[Aj + Ac][0] = CJEX[Aj + Ac][0] + 1440
    CJEX[Aj + Ac][1] = CJEX[Aj + Ac][1] + 1440
    gaps = list()
    for a in range(Ac + Aj):
        if CJEX[a][2] == CJEX[a+1][2]:
            gaps.append([CJEX[a][2], a, CJEX[a][1],
                         CJEX[a+1][0] - CJEX[a][1]])
    gaps = sorted(gaps, key = itemgetter(3))
    
    for g in range(len(gaps)):
        if 'C' == gaps[g][0]:
            if CT + gaps[g][3] <= 720:
                CJEX[gaps[g][1]][2] = 'CF'
                CT = CT + gaps[g][3]
                gaps[g][0] = 'F'
        else:
            if JT + gaps[g][3] <= 720:
                CJEX[gaps[g][1]][2] = 'JF'
                JT = JT + gaps[g][3]
                gaps[g][0] = 'F'
    res = 0
    a = 0
    while a < Aj + Ac:
        if 'CF' == CJEX[a][2] or 'JF' == CJEX[a][2]:
            a = a + 1
            continue
        if CJEX[a][2][0] == CJEX[a + 1][2][0]:
            res = res + 2
            a = a + 1
            continue
        res = res + 1
        a = a + 1
    fout.write('Case #' + str(i + 1) + ': ')
    fout.write(str(res) + '\n')
        
fin.close()
fout.close()
