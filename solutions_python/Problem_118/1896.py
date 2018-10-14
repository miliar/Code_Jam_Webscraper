
def isP(x):
    x = str(x)
    for i in xrange(len(x)):
        if(x[i] == x[len(x)-1-i]):
            pass
        else:
            return False
    return True;

import math
def isS(n):
    if not ( ( isinstance(n, int) or isinstance(n, long) ) and ( n >= 0 ) ):
        return False
    else:
        nsqrt = math.sqrt(n)
        return nsqrt == math.trunc(nsqrt)


inp = open("C-small-attempt0.in", "r")
T = int(inp.readline())
for t in xrange(T):
    tmp = inp.readline().replace("\n", "").split(" ")
    A = int(tmp[0])
    B = int(tmp[1])
    #print A, B
    cnt = 0
    for x in range(A,B+1):
        if isS(x) and isP(x):
            if isP(int(math.sqrt(x))):
                #print x
                cnt += 1
    print "Case #"+ str(t+1) + ": " + str(cnt)