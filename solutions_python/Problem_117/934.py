#/bin/python
import sys

def checkCut(A):
    lenx = len(A)
    leny = len(A[0])

    for i in xrange(0, lenx):
        for j in xrange(0, leny):
            pointer = A[i][j]
            hasTwo = 0
            for p in xrange(0, lenx):
                if A[p][j] > pointer:
                    hasTwo = hasTwo + 1
                    break
            for p in xrange(0, leny):
                if A[i][p] > pointer:
                    hasTwo = hasTwo + 1
                    break
            if hasTwo >= 2:
                return False
    
    return True

num = int(sys.stdin.readline())

count = 1

while num > 0:
    N, M = [int(x) for x in sys.stdin.readline().strip().split(" ")]
    A = []
    for i in xrange(0, N):
        A.append([int(y) for y in sys.stdin.readline().strip().split(" ")])
    r = "NO"
    r1 = checkCut(A)
    if r1 == True:
        r = "YES"
    result = "Case #" + str(count) + ": " + r
    print result
    num = num - 1
    count = count + 1

