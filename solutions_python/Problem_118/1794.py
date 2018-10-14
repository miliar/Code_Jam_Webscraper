"""C
   Google CodeJam 2013
"""

from datetime import datetime
from math import sqrt


def palindrome(si):
    for d in xrange(len(si)/2):
        if si[0+d] != si[-(1+d)]:
            return False
    return True

def routine(A,B):
    found = 0
    i = A
    while i <= B:
        si = str(i)
        if palindrome(si):
            ri = sqrt(i)
            if ri == int(ri):
                sri = str(int(ri))
                if palindrome(sri):
                    found += 1
        
        i+=1
    
    return found

if __name__ == '__main__':
    filename = "C-small-attempt0"  #C-large
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        A, B = [int(x) for x in f.readline().split()]
        
        print A, B

        print >>fo, "Case #%d: %s" % (case+1, routine(A, B))

    fo.close()
    f.close()
    print datetime.now()
