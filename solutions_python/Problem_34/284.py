"""A
   Google CodeJam 2009
"""

from datetime import datetime
import re

makereg = re.compile(r'(\([a-z]+\))')

def routine(words, pattern):
    def addpipe(x):
        return "("+"|".join(x.group()[1:-1])+")"
    
    #convert pattern to regex
    reg_pattern = makereg.sub(addpipe, pattern)
    p = re.compile(reg_pattern)

    c = 0
    for word in words:
        if p.match(word):
            c += 1

    print c
    return c

if __name__ == '__main__':
    filename = "A-large" #Atest
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    L, D, N = [int(x) for x in f.readline().split()]

    print L, D, N

    words = []
    for word in xrange(D):
        words.append(f.readline().strip())
    print words
            
    c = N
    print c, "cases"
    for case in xrange(c):
        pattern = f.readline().strip()

        print
        print pattern

        print >>fo, "Case #%d: %s" % (case+1, routine(words, pattern))

    fo.close()
    f.close()
    print datetime.now()
