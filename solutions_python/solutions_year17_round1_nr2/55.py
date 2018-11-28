#!python3

import math

inputFile = open("B-large.in", "r")
outputFile = open("output.txt", "w")

testCases = int(inputFile.readline())

for testCase in range(1, testCases + 1):

    inp = inputFile.readline().split()

    N = int(inp[0])
    P = int(inp[1])

    R = []
    pack = []

    inp = inputFile.readline().split()
    for i in inp:
        R.append(int(i))
    for i in range(N):
        lst = inputFile.readline().split()
        pck = []
        for j in lst:
            qty = int(j)
            srv = qty / R[i]
            lo = math.ceil(srv / 1.1)
            hi = math.floor(srv / 0.9)

            if hi < lo:
                lo = 0
                hi = 0
            pck.append([lo, hi])

        pck.sort()
        pack.append(pck)

    index = [0] * N


    ans = 0
    outOfPack = False

    for i in range(N):
        while index[i] < P and pack[i][index[i]][0] == 0:
            index[i] = index[i] + 1

    while True:
        for i in index:
            if i >= P:
                outOfPack = True
                break

        if outOfPack:
            break

        MinMax = 0
        MinServe = pack[0][index[0]][0]
        MaxServe = pack[0][index[0]][1]
        
        for i in range(1, N):
            MinServe = max(MinServe, pack[i][index[i]][0])
            MaxServe = min(MaxServe, pack[i][index[i]][1])

            if pack[MinMax][index[MinMax]][1] > pack[i][index[i]][1]:
                MinMax = i
            
        if MinServe <= MaxServe:
            ans += 1
            for i in range(N):
                index[i] = index[i] + 1
            continue

        index[MinMax] += 1

        

    print("Case #", testCase, ": ", ans, sep="", file=outputFile)

inputFile.close()
outputFile.close()
