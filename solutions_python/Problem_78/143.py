import sys

def isInt(f):
    if f - int(f) == 0:
        return 1
    return 0

def test1(N,Pd):
    i = 1
    while (i <= N):
        if isInt(i * Pd / 100.):
            return 1
        i += 1
    return 0

def doit(N, Pd, Pg):
    #print N, Pd, Pg
    #Impossible Case 1
    if Pd != 100 and Pg == 100:
        return 0

	#Impossible Case 2
    if Pd != 0 and Pg == 0:
        return 0

	#Impossible Case 3
    if Pd == 0 and Pg == 0:
        return 1

    
    #test1
    ret1 = test1(N, Pd)
    if ret1 == 1:
        return 1
    #test2
    ret2 = test1(N, Pd)
    if ret2 == 1:
        return 1
    
    return 0

if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = open(sys.argv[1], "r")
        T = int(f.readline().strip())
        for _t in range(T):
            N, Pd, Pg = map(int, f.readline().strip().split())
            ret = doit(N, Pd, Pg)
            print "Case #%d: %s" %(_t + 1, ["Broken", "Possible"][ret])
        f.close()
