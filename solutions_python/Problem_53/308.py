from util import *
import psyco
psyco.full()

def main():
    cases = int(raw_input())
    for i in xrange(0, cases):
        N, k = map(int, raw_input().split(" "))
        res = "OFF"
        if (k+1)%(2**N) == 0:
            res = "ON"
        print "Case #%i: %s" % (i+1, res)
    
            
main()