"""
QR2011
http://code.google.com/codejam/contest/dashboard?c=975485#
"""

if __name__ == "__main__":
    f = open('A-large.in')
#    f = open('test.in')
    T = int(f.readline())
    for t in range(T):
        data = f.readline().split()
        N = int(data[0])
        actions = []
        for n in range(N):
            actions += [(data[n*2+1], int(data[n*2+2]))]
        po,pb = 1,1
        do,db = 0,0
        s = 0
        for r,p in actions:
            if r == 'O':
                if abs(p - po) < do:
                    ds = 1
                else:
                    ds = abs(p - po) - do + 1
                do = 0
                db += ds
                po = p
            elif r == 'B':
                if abs(p - pb) < db:
                    ds = 1
                else:
                    ds = abs(p - pb) - db + 1
                do += ds
                db = 0
                pb = p
            s += ds
    
        print "Case #%d: %d" % (t+1, s)
