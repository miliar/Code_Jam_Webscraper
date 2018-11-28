import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        a,b,c = f.readline().strip("\r\n").split()
        
        c = int(c)
        count = 0
        for aa in xrange(int(a)):
            for bb in xrange(int(b)):
                if aa & bb < c:
                    count += 1
                    
        print "Case #%d: %s" % (caseno+1, str(count))
        
main()