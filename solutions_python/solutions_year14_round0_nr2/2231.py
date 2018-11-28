import sys

T = int(raw_input())

for i in xrange(T):
        sys.stdout.write('Case #%d: ' % (i+1))
        C, F, X = [float(x) for x in raw_input().split()]
        t = 0
        s = 2.0
        while True:
                t1 = C/s + X/(s+F)
                t2 = X/s
                if t1 < t2:
                        t += C/s
                        s += F
                else:
                        t += t2
                        print t
                        break
        
