import sys

inf = open('D2.in','r')

T = [int(x) for x in inf.readline().split()][0]

for t_case in range(1,T+1):
    X,R,C = [int(x) for x in inf.readline().split()]
    if R < C:
        K = R
        R = C
        C = K
        
    ret = 0
    if X == 1:
        ret = 1
    elif X == 2:
        if (R*C % 2) > 0:
            ret = -1
        else:
            ret = 1
    elif X == 3:
        if C == 1:
            ret = -1
        elif C == 2:
            if R == 3:
                ret = 1
            else:
                ret = -1
        elif C == 3:
            if R == 3:
                ret = 1
            else:
                ret = 1
        else:
            ret = -1
    elif X == 4:
        if C == 1 or C == 2:
            ret = -1
        elif R == 4:
            ret = 1
        else:
            ret = -1
    
    if ret == -1:
        fin = "RICHARD"
    else:
        fin = "GABRIEL"
    
    print "Case #%d: %s" % (t_case, fin)
