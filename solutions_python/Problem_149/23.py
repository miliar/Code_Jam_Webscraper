import sys
from collections import deque


import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        n = int(f.readline().strip("\r\n"))
            
        numbers = []
        for a in f.readline().strip("\r\n").split():
            a = int(a)
            numbers.append(a)

        swaps = 0
        while len(numbers) > 0:
            low = None
            lowpos = None
            for i in xrange(len(numbers)):
                if low is None or numbers[i] < low:
                    low = numbers[i]
                    lowpos = i
                    
            swaps += min(lowpos, len(numbers) - lowpos - 1)
            numbers.pop(lowpos)
        
        print "Case #%d: %d" % (caseno+1, swaps)
        
main()