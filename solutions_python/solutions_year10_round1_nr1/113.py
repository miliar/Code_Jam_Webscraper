inFile = open("../A-large.in", "r")
outFile = open("../A-sol.txt", "w")

numTests = int(inFile.readline().strip())
board = []

def countK(board, i, j, c, dim, k):
    #print "trying: " + str(i) + " " + str(j)
    
        
    if i <= dim - k:
        found = True
        for it in range(k):
            found = found and board[i + it][j] == c
            if not found:
                break
        if found:
            return True
    
    if j <= dim - k:
        found = True
        for jt in range(k):
            found = found and board[i][j+jt] == c
            if not found:
                break
        if found:
            return True
    
    if i <= dim - k and j <= dim - k:
        found = True
        for it in range(k):
            found = found and board[i + it][j + it] == c
            if not found:
                break
        if found:
            return True
    
    if i <= dim - k and j <= dim - k:
        found = True
        for it in range(k):
            found = found and board[i + it][(j + k - 1) - it] == c
            if not found:
                break
        if found:
            return True
    return False

for testNum in range(numTests):
    dim, k = map(int, inFile.readline().split())
    board = []
    rFound = bFound = False
    for i in range(dim):
        row = inFile.readline().rstrip()
        board.append(row)
    
    for i in range(dim):
        row = board[i]
        row = row.replace(".", "")
        numToAdd = dim - len(row)
        row = "".join(["." for x in range(numToAdd)]) + row
        board[i] = row
    
    for i in range(dim):
        for j in range(dim):
            if not rFound:
                rFound = countK(board, i, j, "R", dim, k)
            if not bFound:
                bFound = countK(board, i, j, "B", dim, k)
            if rFound and bFound:
                break
        if rFound and bFound:
            break
       
    result = "" 
    if not (rFound or bFound):
        result = "Neither"
    elif rFound and not bFound:
        result = "Red"
    elif bFound and not rFound:
        result = "Blue"
    else:
        result = "Both"
    outFile.write("Case #" + str(testNum+1) + ": " + result + "\n")
    print "Case #" + str(testNum+1) + ": " + result