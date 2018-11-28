import sys

def is_possible(N, Pd, Pg):
    for D in xrange(1, N+1):
        # Pg can be anything except not 100 if Pd<100 and not 0 if Pd>0
        if (D*Pd)%100==0:
            if (Pg==100 and Pd<100) or (Pg==0 and Pd>0):
                pass
            else:
                return True
    return False
    

infile = sys.stdin

T = int(infile.readline())
for i in xrange(T):
    N, Pd, Pg = map(int, infile.readline().split())
    result = is_possible(N, Pd, Pg)
    print("Case #%d: %s" % (i+1, "Possible" if result else "Broken"))