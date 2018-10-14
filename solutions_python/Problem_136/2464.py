import math
T = int(raw_input())
for i in range(1,T+1):
    C,F,X = map(float,raw_input().split())
    minN = (X/C) - (2/F) - 1
#    print minN
    N = 0
    if minN <= 0:
        print "Case #" + str(i) + ": " + str(X/2)
        continue;
    else:   
        N = int(math.ceil(minN))
    res = 0
#    print N
    for k in range(0,N):
        res += C/float(2+float(F*k))
    res += X/float(2+float(N*F))
    print "Case #" + str(i) + ": " + str(res)
    
