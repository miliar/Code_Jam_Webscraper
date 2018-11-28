import math
def fs(x):
    if (str(x)[::-1] == str(x)):
        if int(math.sqrt(x))**2==x:
            if str(int(math.sqrt(x)))[::-1] == str(int(math.sqrt(x))):
                return True
    return False

T = int(raw_input())
for t in range(T):
    print "Case #"+str(t+1)+":",
    A,B = map(int,raw_input().split())
    tot = 0
    for i in xrange(A,B+1):
        if fs(i):
            tot+=1
    print tot
    
