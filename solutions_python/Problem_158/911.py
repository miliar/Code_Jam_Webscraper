import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for i in range(T):
        [X, R, C] = [int(val) for val in f.readline().split()]
        if X == 1:
            print "Case #"+str(i+1)+": GABRIEL"
        elif X == 2:
            if R %2 == 1 and C %2 == 1 :
                print "Case #"+str(i+1)+": RICHARD"
            else:
                print "Case #"+str(i+1)+": GABRIEL"
        elif X == 3:
            if R == 1 or C == 1 or (R < 3 and C < 3):
                print "Case #"+str(i+1)+": RICHARD"
            elif (R == 2 and C ==4) or (R == 4 and C ==2) :
                print "Case #"+str(i+1)+": RICHARD"
            elif (R==4 and C == 4):
                print "Case #"+str(i+1)+": RICHARD"
            else:
                print "Case #"+str(i+1)+": GABRIEL"
        else:
            if (R < 4 and C < 4):
                print "Case #"+str(i+1)+": RICHARD"
            elif (R == 1 or C == 1):
                print "Case #"+str(i+1)+": RICHARD"
            elif R == 2 or C == 2:
                print "Case #"+str(i+1)+": RICHARD"
            else:
                print "Case #"+str(i+1)+": GABRIEL"
                
                
                
            
