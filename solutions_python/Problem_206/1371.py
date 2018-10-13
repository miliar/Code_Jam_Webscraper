from operator import itemgetter

fin = open('A-large.in')
fout = open('A_out.txt', 'w')
T = int(fin.readline().split()[0])
print(T)

for i in range(T):
    dataIn = fin.readline().split()
    D = int(dataIn[0])
    N = int(dataIn[1])
    KS = list()
    for h in range(N):
        dataIn = fin.readline().split()
        KS.append([int(dataIn[0]), int(dataIn[1])])
    KS = sorted(KS, key = itemgetter(0), reverse = True)
    t = 0;
    for h in range(0, N):
        K = KS[h][0]
        S = KS[h][1]
        if (D - K) / S > t:
            t = (D - K) / S
    fout.write('Case #' + str(i + 1) + ': ' + str(D/t)
               + '\n')
        
fin.close()
fout.close()
