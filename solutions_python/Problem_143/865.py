import sys
f = open(sys.argv[1])
T = int(f.readline())

for t in range(T):
    P = []
    A = []
    B = []
    K = []
    count = 0
    P += [map(int,f.readline().split())]
    A = P[0][0]
    B = P[0][1]
    K = P[0][2]
    if A > B:
        temp = A
        A = B
        B = temp        
    if A == B:
        for i in xrange(0,A-1):
            for j in xrange(i,B):
                if i & j < K:
                    count = count+1
                    if j < A:
                        if j != i:
                            count = count+1
        if A-1 & B-1 < K:
            count = count+1
    else:
        for i in xrange(0,A):
            for j in xrange(i,B):
                if i & j < K:
                    count = count+1
                    if j < A:
                        if j != i:
                            count = count+1
    print "Case #%d: %d" % (t+1,count)
