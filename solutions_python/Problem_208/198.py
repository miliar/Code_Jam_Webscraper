import sys

inputName = "C-input.txt"

if (len(sys.argv)>1):
    inputName = sys.argv[1]

inFile = open(inputName, "rt")
outFile = open(inputName+".out", "wt")

T = int(inFile.readline())
for testCase in range(1, T + 1):
    outFile.write("Case #"+str(testCase)+": ")
    line = inFile.readline().strip().split()
    N = int(line[0])
    Q = int(line[1])
    E=[]
    S=[]
    for j in range (N):
        line = inFile.readline().strip().split()
        E.append(int(line[0]))
        S.append(int(line[1]))

    D=[]
    for j in range (N):
        line = inFile.readline().strip().split()
        row = []
        for k in range (N):
            row.append(int(line[k]))
        D.append(row)

    U=[]
    V=[]
    for j in range (Q):
        line = inFile.readline().strip().split()
        U.append(int(line[0])-1)
        V.append(int(line[1])-1)
        

    minTime=[-1]*N
    minTime[N-1] = 0
    for i in range(N-1):
        current = N-2 - i
        for junction in range(current+1, N):
            distance = 0
            for k in range(current, junction):
                distance += D[k][k+1]
            if (E[current] >= distance):
                tmpTime = (float(distance) /  S[current]) + minTime[junction]
                if (minTime[current]<0) or (minTime[current]>tmpTime):
                    minTime[current] = tmpTime
        

    outFile.write(str(minTime[0])+"\n")

inFile.close()
outFile.close()


