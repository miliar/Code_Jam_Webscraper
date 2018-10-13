lawns = int(raw_input())
for l in range(lawns):
    line = raw_input().split(' ')
    N = int(line[0])
    M = int(line[1])
    rowMaxs = []
    colMaxs = []
    lawn = []
    for i in range(N):
        lawn.append([])
        line = raw_input().split(' ')
        for j in range(M):
            lawn[i].append(int(line[j]))
    for i in range(N):
        tmpMax = 0
        for j in range(M):
            if(tmpMax < lawn[i][j]):
                tmpMax = lawn[i][j]
        rowMaxs.append(tmpMax)
    for i in range(M):
        tmpMax = 0
        for j in range(N):
            if(tmpMax < lawn[j][i]):
                tmpMax = lawn[j][i]
        colMaxs.append(tmpMax)
    lawnPass = 1
    for i in range(N):
        for j in range(M):
            if(rowMaxs[i] > colMaxs[j]):
                if not (colMaxs[j] == lawn[i][j]):
                    lawnPass = 0
            else:
                if not (rowMaxs[i] == lawn[i][j]):
                    lawnPass = 0
    texRes = ""
    if(lawnPass):
        texRes = "YES"
    else:
        texRes = "NO"
    print "Case #" + repr(l + 1) + ": " + texRes
