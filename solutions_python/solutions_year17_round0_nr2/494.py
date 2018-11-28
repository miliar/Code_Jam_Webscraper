import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        number = [int(x) for x in f.readline().strip()]
        
        while True:
            bad = False
            for i in xrange(len(number)-1):
                if number[i] > number[i+1]:
                    bad = True
                    for j in xrange(i+1, len(number)):
                        number[j] = 9
                        
                    number[i] -= 1
                
            if not bad:
                break
                
        res = int("".join([str(x) for x in number]))
            
        print "Case #%d: %d" % (caseno+1, res)
        
main()