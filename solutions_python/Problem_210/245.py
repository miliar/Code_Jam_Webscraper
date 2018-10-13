import sys
import glob, os

def solve_file(filen):
    f = open(filen + '.in', 'r')
    T = int(f.readline())

    ans = ""

    for i in range(1, T+1):
        line = f.readline().split(" ")

        AC = int(line[0])
        AJ = int(line[1])
        C = [];
        D = [];
        J = [];
        K = [];

        for j in range(AC):
            line = f.readline().split(" ")
            C.append(int(line[0]))
            D.append(int(line[1]))
        for j in range(AJ):
            line = f.readline().split(" ")
            J.append(int(line[0]))
            K.append(int(line[1]))

        C = sorted(C)
        D = sorted(D)
        J = sorted(J)
        K = sorted(K)

        nans = solve_cks(AC,AJ,C,D,J,K)

        ans += "Case #%d: %s\n" % (i, nans)

    f = open(filen + '.out', 'w')
    f.write(ans)
    print(ans)

def solve_cks(AC,AJ,C,D,J,K):
    if len(C) < len(J):
        tmp1 = C
        tmp2 = D
        C = J
        D = K
        J = tmp1
        K = tmp2

    t = [d-c for (d, c) in zip(D, C)]
    tC = sum(t)
    tl = 720 - tC

    # Find gaps
    gps = []
    gpsz = []

    if len(J) == 0 or (C[0] < J[0] and D[-1] > K[-1]):
        if C[0] > 0 or D[-1] < 1440:
            gps.append(-1)
            gpsz.append(1440 - D[-1] + C[0])
            #print("ww")
            #print(1440 - D[-1] + C[0])
            #print(tl)

    jind = 0
    for i in range(len(C)-1):
        if len(J) > 0 and D[i] < J[-1]:
            while J[jind] < D[i]:
                jind += 1

        if len(J) == 0 or C[i+1] < J[jind]:
            gps.append(i)
            gpsz.append(C[i+1]-D[i])

    n = 0

    gpszS = sorted(gpsz)
    gpszSi = sorted(range(len(gpsz)), key=lambda x: gpsz[x])
    gci = []

    createGaps = True
    tlae = tl - sum(gpsz)
    if tlae <= 0:
        createGaps = False

    for i in range(len(gpszS)):
        gz = gpszS[i]
        if tl - gz >= 0:
            if gps[gpszSi[i]] == -1:
                print("--")
                if gz == 0:
                    print(C)
                    print(D)
                print(tl)
                print(gz)

            tl -= gz
            n += 2
            gci.append(gps[gpszSi[i]])
        else:
            break

    for i in gci:
        if i == -1:
            C[0] = 0
            D[-1] = 1440
        else:
            D[i] = C[i+1]

    ind = 0
    while ind < len(C)-1:
        if D[ind] == C[ind+1]:
            D.pop(ind)
            C.pop(ind+1)
        else:
            ind += 1

    #print(gci)
    #print(C)
    #print(D)

    noptim = 2*len(C)
    if D[-1] == 1440 and C[0] == 0:
        noptim -= 2

    if ~createGaps:
        if noptim == 0:
            print(C)
            print(D)
        return noptim

    jind = 0
    gpsR = []
    gpszR = []

    if (J[0] < C[0] and K[-1] > D[-1]):
        if J[0] > 0 or K[-1] < 1440:
            gpsR.append(-1)
            gpszR.append(1440 - J[-1] + K[0])

    for i in range(len(J) - 1):
        while jind < len(C) and C[jind] < K[i]:
            jind += 1

        if jind >= len(C) or K[i + 1] < C[jind]:
            gpsR.append(i)
            gpszR.append(J[i + 1] - K[i])

    gpszRs = list(reversed(sorted(gpszR)))
    while tlae > 0:
        tlae -= gpszRs.pop(0)
        noptim += 2

    return noptim

if __name__ == '__main__':

    for file in glob.glob("*.in"):
        filen = file[0:-3]
        print(filen)
        solve_file(filen)