fin = open('A-large.in')
#fin = open('A_in.txt')
fout = open('A_out.txt', 'w')
T = int(fin.readline().split()[0])
print(T)

for i in range(T):
    dataIn = fin.readline().split()
    R = int(dataIn[0])
    C = int(dataIn[1])
    cake = []
    for j in range(R):
        dataIn = fin.readline()
        cake.append(list(dataIn))
    initRange = []
    for j in range(R):
        for k in range(C):
            init = cake[j][k]
            if '?' == init:
                continue
            if len(initRange) == 0:
                initRange.append([init, j, k,
                                  0, 0, R-1, C-1])
                continue
            newIrg = [init, j, k, 0, 0, R-1, C-1]
            for l in range(len(initRange)):
                irg = list(initRange[l])
                if (irg[3] <= j and irg[5] >= j and
                    irg[4] <= k and irg[6] >= k):
                    if irg[1] < j:
                        initRange[l][5] = j - 1
                        newIrg[4:6 + 1] = list(irg[4:6 + 1])
                        newIrg[3] = j
                        break
                    if irg[2] < k:
                        initRange[l][6] = k - 1
                        newIrg[3:6 + 1] = list(irg[3:6 + 1])
                        newIrg[4] = k
                        break
                    if irg[2] > k:
                        initRange[l][4] = irg[2]
                        newIrg[3:6 + 1] = list(irg[3:6 + 1])
                        newIrg[6] = irg[2] - 1
                    break
            initRange.append(newIrg)
    for l in range(len(initRange)):
        irg = initRange[l]
        for j in range(irg[3], irg[5] + 1):
            for k in range(irg[4], irg[6] + 1):
                cake[j][k] = irg[0]
                            
    fout.write('Case #' + str(i + 1) + ':\n')
    for j in range(R):
        for k in range(C):
            fout.write(cake[j][k])
        fout.write('\n')
        
fin.close()
fout.close()
