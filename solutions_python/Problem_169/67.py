import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        n, v, x = f.readline().split()
        n = int(n)
        v = float(v)
        x = float(x)
        
        flows = []
        for i in xrange(n):
            r, c = f.readline().split()
            r = float(r)
            c = float(c)
            flows.append((r,c))
            
        
        if n == 1:
            r, c = flows[0]
            if c != x:
                s = "IMPOSSIBLE"
            else:
                s = str(v / r)
        elif n == 2:
            r0, x0 = flows[0]
            r1, x1 = flows[1]
            
            lo = min(x0, x1)
            hi = max(x0, x1)
            
            if x < lo or x > hi:
                s = "IMPOSSIBLE"
            else:
                if x1 == x0:
                    s = str(v / (r0+r1))
                else:
                    v1 = v*(x-x0)/(x1-x0)
                    time1 = v1 / r1
                    time0 = (v-v1)/ r0
                    s = str(max(time1, time0))

        else:
            print "UNSUPPORTED"
            exit()
            
        

        print "Case #%d: %s" % (caseno+1, s)
        
main()