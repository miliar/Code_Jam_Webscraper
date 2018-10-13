import sys

#with open(sys.argv[1]) as tests:
with open("A-small-attempt0.in") as tests:
    n = int(tests.readline())
    #print n
    for ncase in range(1, n + 1):
        nrow = int(tests.readline()) - 1
        A = []
        for i in range(4):
            line = tests.readline()
            A.append(map(int, line.split()))
        #print A
        rset = set(A[nrow])

        ncol = int(tests.readline()) - 1
        B = []
        for i in range(4):
            line = tests.readline()
            B.append(map(int, line.split()))
        #print B

        cset = set(B[ncol])
        if len(cset & rset) == 1:
            print "Case #%d: %d" % (ncase, list(cset & rset)[0])
        elif len(cset & rset) > 1:
            print "Case #%d: Bad magician!" % ncase
        elif len(cset & rset) == 0:
            print "Case #%d: Volunteer cheated!" % ncase
    
