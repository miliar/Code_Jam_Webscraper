from collections import deque
import time
import math

def main():
    path = "C:\\Users\\user\\Dropbox\\Documents\\GoogleCodeJam2017\\A. Horses\\"
    with open(path + "result" + str(time.time()) + ".txt", 'w') as resF:
        T, N, D, H = readFile(path + "example.txt")#####
        print T
        print N
        print D
        print H
        for i in xrange(T):
            #t = time.time()
            sol = solve(N[i], D[i], H[i])
            resF.write("Case #" + str(i+1) + ": " + "{0:.6f}".format(sol) + "\n")


def solve(N, D, H):
    H2 = sorted(H, key=lambda x: x[0])
    slowest = -1
    i = 0
    while i < N:
        j = findFirstHorseHeMeets(H, i, N, D)
        if j == -1:  # doesnt meet anyone
            slowest = i
            break
        else:
            i = j
    if slowest == -1:
        print "WTF ERROR"
    sj = float(H2[slowest][1])
    kj = float(H2[slowest][0])

    return float((sj*D))/(D-kj)

def findFirstHorseHeMeets(H, i, N, D):
    minimalCrossX = -1
    index = -1
    for j in xrange(i+1, N):
        kj = float(H[j][0])
        ki = float(H[i][0])
        sj = float(H[j][1])
        si = float(H[i][1])
        if si == sj:
            continue
        xij = (kj-ki)/(si-sj)
        yij = (si*kj-sj*ki)/(si-sj)
        if (yij > D) or (xij <= 0):
            continue
        else:
            if minimalCrossX == -1:
                print "WooHoo"
                minimalCrossX = xij
                index = j
            elif minimalCrossX > xij:
                minimalCrossX = xij
                index = j
    return index


def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        if len(lines) == 0:
            print "Err reading"
            return

        T = int(lines[0].replace("\n", ""))

        N = []
        D = []
        H = []
        j = 1
        for i in xrange(1, T+1):
            temp = lines[j].split(" ")

            currN = int(temp[1].replace("\n", ""))
            currH = []
            D.append(int(temp[0]))
            N.append(currN)
            j += 1

            for i2 in xrange(currN):
                temp = lines[j].split(" ")
                currH.append((int(temp[0]), int(temp[1].replace("\n", ""))))
                j += 1

            H.append(currH)


        return (T, N, D, H)

if __name__ == '__main__':
    main()


