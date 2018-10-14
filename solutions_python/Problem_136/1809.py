import sys

for case in xrange(int(sys.stdin.readline())):
    CPS = 2
    farmCost, farmExtraCPS, target = map(float, sys.stdin.readline().split())
    
    t = 0
    while True:
        if (( target/CPS) < (farmCost/CPS + target/(CPS+farmExtraCPS)) ):
            # its faster to not buy a farm
            t += target/CPS
            break
        else:
            # buy a farm
            t += farmCost/CPS
            CPS += farmExtraCPS

    print "Case #"+str(case+1)+": " + str(t)
