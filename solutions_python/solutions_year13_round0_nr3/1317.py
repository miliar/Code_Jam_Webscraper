import sys
import math

def FairSquare(Min, Max):
    def checkFair(n):
        s = str(n)
        for i in range(0, len(s)/2):
            if s[i] != s[-1-i]:
                return False
        return True

    result = 0
    sMin = int(math.floor(math.sqrt(Min)))
    if sMin>1:
        sMin = sMin -1
    sMax = int(math.ceil(math.sqrt(Max))) + 1
    for i in range(sMin, sMax+1):
        ii = i * i
        if Min<=ii and ii<=Max and checkFair(i) and checkFair(ii):
            result = result + 1
    return result

if len(sys.argv)<2:
    exit()
with open(sys.argv[1]) as f:
    N = int(f.readline())
    for i in range(1, N+1):
        Min, Max = [int(x) for x in f.readline().split()]
        print 'Case #'+str(i)+': '+str(FairSquare(Min, Max))

