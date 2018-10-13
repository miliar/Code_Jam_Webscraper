
INPUT_FILE_PATH = "A-large.in"
OUTPUT_FILE_PATH = "out.txt"

f = open(INPUT_FILE_PATH, "r")
of = open(OUTPUT_FILE_PATH,'w')

def solve():
    #=====================================
    dotFound = False
    #line matching
    hashDiagTopLeft = 0
    hashDiagTopRight = 0
    for i in range(0,4):
        hashValueX = 0
        hashValueY = 0
        for j in range(0,4):
            #row
            if A[i][j] == 'X': hashValueX += 1
            elif A[i][j] == 'O': hashValueX += 10
            elif A[i][j] == 'T': hashValueX += 100
            else: dotFound = True
            #column
            if A[j][i] == 'X': hashValueY += 1
            elif A[j][i] == 'O': hashValueY += 10
            elif A[j][i] == 'T': hashValueY += 100
            else: dotFound = True
            #diag TOP LEFT
            if (i==j):
                if A[i][j] == 'X': hashDiagTopLeft += 1
                elif A[i][j] == 'O': hashDiagTopLeft += 10
                elif A[i][j] == 'T': hashDiagTopLeft += 100
                else: dotFound = True
            #diag TOP RIGHT
            if (i==3-j):
                if A[i][j] == 'X': hashDiagTopRight += 1
                elif A[i][j] == 'O': hashDiagTopRight += 10
                elif A[i][j] == 'T': hashDiagTopRight += 100
                else: dotFound = True
        if (hashValueX == 4 or hashValueX == 103): return "X won"
        if (hashValueX == 40 or hashValueX == 130): return "O won"
        if (hashValueY == 4 or hashValueY == 103): return "X won"
        if (hashValueY == 40 or hashValueY == 130): return "O won"
        if (hashDiagTopLeft == 4 or hashDiagTopLeft == 103): return "X won"
        if (hashDiagTopLeft == 40 or hashDiagTopLeft == 130): return "O won"
        if (hashDiagTopRight == 4 or hashDiagTopRight == 103): return "X won"
        if (hashDiagTopRight == 40 or hashDiagTopRight == 130): return "O won"
    #diagonal
    
    if dotFound:
        return "Game has not completed"
    else:
        return "Draw"
    #=====================================

# -------------------------------------------------
T = int(f.readline().strip())

for C in range(1,T+1):
    # problem = 
    A = []
    for i in range(0,4):
        A.append(f.readline().strip())
    f.readline().strip()

    # solution
    of.write( "Case #"+str(C)+": "+solve()+"\n");
    print "DONE"

# -------------------------------------------------


