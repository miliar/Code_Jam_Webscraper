import sys
l = sys.stdin.readline()
T = int(l.strip())
#print "T = %d" %(T)
n = 1
for l in sys.stdin.readlines():
    Bp = Op = 1 # Blue and Orange initial position
    Time = 0
    Elapse = 0
    d = l.strip().split(" ")
    #print d
    N = int(d[0])
    #print "N = %d" %(N)
    lastColor = "A"
    for i in range(0, N):
        index = 1 + i * 2;
        R = d[index]
        P = int(d[index + 1])
        dist = 0
##        print "i = %d" %(i)
        if Elapse <> 0 and R <> lastColor:
            if R == "B":
                if abs(Bp - P) < Elapse:
                    Bp = P
                elif Bp > P:
                    Bp -= Elapse
                else:
                    Bp += Elapse
##                print "Bp = %d" %(Bp)

            else:
                if abs(Op - P) < Elapse:
                    Op = P
                elif Op > P:
                    Op -= Elapse
                else:
                    Op += Elapse
##                print "Op = %d" %(Op)
            Elapse = 0
            
        if R == "B":
            dist = abs(Bp - P)
            Bp = P
##            print "Bp = %d" %(Bp)
        else:
            dist = abs(Op - P)
            Op = P
##            print "Op = %d" %(Op)

        Time += dist + 1
##        print "Time = %d" %(Time)
        
        Elapse += dist + 1

##        print "Elapse = %d" %(Elapse)
        lastColor = R
    print "Case #%d: %d" %(n, Time)
    n += 1
