fin = open('A-small-attempt0.in')
fout = open('A_out.txt', 'w')

T = int(fin.readline().split()[0])

for t in range(T):
    dataIn = fin.readline().split()
    N = int(dataIn[0])
    P = int(dataIn[1])
    dataIn = fin.readline().split()
    G = [0, 0, 0, 0]
    for i in range(len(dataIn)):
        g = int(dataIn[i]) % P
        G[g] = G[g] + 1
    res = G[0]
    if 2 == P:
        res = res + G[1] // 2
        if G[1] % 2 > 0:
            res = res + 1
    elif 3 == P:
        if G[1] <= G[2] :
            res = res + G[1]
            S = G[2] - G[1]
        else:
            res = res + G[2]
            S = G[1] - G[2]
        res = res + S // 3
        if S % 3 > 0:
            res = res + 1

    fout.write('Case #' + str(t + 1) + ': ' + str(res) + '\n')

fin.close()
fout.close()