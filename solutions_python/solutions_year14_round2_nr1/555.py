import sys


def getCharsAndCount(inp, l, c):
    length = len(inp)
    l.append(inp[0])
    count = 1
    for i in range(1,length):
        if (inp[i] == inp[i-1]):
            count = count + 1
        else:
            c.append(count)
            count = 1
            l.append(inp[i])
    c.append(count)

def checkPossible(L, N):
    if (len(L) != N):
        print "incorrect input to checkPossible"
        
    for i in range(1,N):
        if (L[i] != L[0]):
            return False
    
    return True
    
def getMoves(C,N):
    if (len(L) != N):
        print "incorrect input to getMoves"
    
    length = len(C[0])
    ret = 0
    for j in range(0,length):
        sum1 = 0
        for i in range(0,N):
            sum1 = sum1 + C[i][j]
        mean = int(round ((1.0 * sum1) / N))
#         print "mean is " + str(mean)
        for i in range(0,N):
            ret = ret + abs(mean - C[i][j])

    return ret

T = int (sys.stdin.readline())

for case in range(1,T+1):
    N = int (sys.stdin.readline())
    L = []
    C = []
    for i in range(0,N):
        input1 = sys.stdin.readline().strip()
        chars = []
        counts = []
        getCharsAndCount(input1, chars, counts)
        L.append(chars)
        C.append(counts)
        
    
#     print L
#     print C
    
    if (not checkPossible(L, N)):
        print "Case #" + str(case) + ": " + "Fegla Won"
    else:
        print "Case #" + str(case) + ": " + str(getMoves(C,N))
        