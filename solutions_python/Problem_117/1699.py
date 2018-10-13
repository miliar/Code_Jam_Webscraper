def p2(inName, outName):
    inFile = open(inName, "r")
    outFile = open(outName, "w")
    T = int(inFile.readline())
    for t in range(T):
        N, M = map(int, inFile.readline().split())
        lawn = []
        for _ in range(N):
            lawn.append(map(int, inFile.readline().split()))
        if violate(lawn, outFile, t, N, M):
            outFile.write("Case #" + str(t+1) + ": NO")
        else:
            outFile.write("Case #" + str(t+1) + ": YES")
        outFile.write("\n")
                
def violate(lawn, outFile, t, N, M):
    if N == 1 or M == 1:
        return False
    for i in range(0, N):
        for j in range(0, M):
            rowNeighbors = []
            if j == 0:
                rowNeighbors.append([i, j+1])
            elif j == M-1:
                rowNeighbors.append([i, j-1])
            else:
                rowNeighbors.append([i, j+1])
                rowNeighbors.append([i, j-1])
                   
            colNeighbors = []
            if i == 0:
                colNeighbors.append([i+1, j])
            elif i == N-1:
                colNeighbors.append([i-1, j])
            else:
                colNeighbors.append([i+1, j])
                colNeighbors.append([i-1, j])
        
            for i1, j1 in rowNeighbors:
                if lawn[i1][j1] < lawn[i][j] and violateCol(lawn, j1, N):
                    print 1, i, j
                    return True
                if lawn[i1][j1] > lawn[i][j] and violateCol1(lawn, i1, j1, M, N):
                    print 2, i, j
                    return True
                    
            for i1, j1 in colNeighbors:
                if lawn[i1][j1] < lawn[i][j] and violateRow(lawn, i1, M):
                    print 3, i, j
                    return True
                if lawn[i1][j1] > lawn[i][j] and violateRow1(lawn, i1, j1, M, N):
                    print 4, i, j
                    return True
    return False
def violateCol(lawn, j, N):
    for i in range(1, N):
        if lawn[i][j] != lawn[i-1][j]:
            return True
    return False

def violateCol1(lawn, i, j, M, N):
    for i1 in range(N):
        if lawn[i1][j] > lawn[i][j]:
            return True
        if lawn[i1][j] == lawn[i][j]:
            continue
        if violateRow(lawn, i1, M):
            return True      
    return False

def violateRow(lawn, i, M):
    for j in range(1, M):
        if lawn[i][j] != lawn[i][j-1]:
            return True
    return False

def violateRow1(lawn, i, j, M, N):
    for j1 in range(M):
        if lawn[i][j1] > lawn[i][j]:
            return True
        if lawn[i][j1] == lawn[i][j]:
            continue
        if violateCol(lawn, j1, N):
            return True
    return False
#p2('intestp3.txt', 'B-small-attempt3.out_')
p2('B-small-attempt4.in', 'B-small-attempt4.out')
            