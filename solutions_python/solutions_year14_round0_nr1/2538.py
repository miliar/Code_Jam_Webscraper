"""A
   Google CodeJam 2014
"""

from datetime import datetime


def routine(A1, C1, A2, C2):
    r1 = C1[A1-1]
    r2 = C2[A2-1]
    common = r1 & r2
    if len(common) == 1:
        return common.pop()
    elif common:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"
        

if __name__ == '__main__':
    filename = "A-small-attempt0"  #-small-attempt0 -large
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        A1 = int(f.readline())
        C1 = []
        for i in xrange(4):
            c = set([int(x) for x in f.readline().split()])
            C1.append(c)
        A2 = int(f.readline())
        C2 = []
        for i in xrange(4):
            c = set([int(x) for x in f.readline().split()])
            C2.append(c)
        
        #print A1, C1, A2, C2

        print >>fo, "Case #%d: %s" % (case+1, routine(A1, C1, A2, C2))

    fo.close()
    f.close()
    print datetime.now()
