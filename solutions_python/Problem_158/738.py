for case in range(int(raw_input())):
    X, R, C = map(int ,raw_input().split())
    res = False
    if X == 1:
        res = True
    elif X == 2:
        if R*C % 2 == 0:
            res = True
        else:
            res = False
    elif X == 3:
        if R*C % 3 != 0 or R*C == 3:
            res = False
        else:
            res = True
    else: #4
        if R*C % 4 != 0:
            res = False
        elif R*C == 12 or R*C == 16:
            res = True
        else:
            res = False
            
    if res == True:    
        print "Case #%d: %s" % (case+1, "GABRIEL")
    else:
        print "Case #%d: %s" % (case+1, "RICHARD")

