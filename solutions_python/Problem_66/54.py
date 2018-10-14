import sys
f = open(sys.argv[1])
cases = int(f.readline())
for case in range(1,cases+1):
    P = int(f.readline())
    M = [ int(v) for v in f.readline().split() ]
    R = []
    T = [] # tickets
    for r in range(P):
        R.append([int(v) for v in f.readline().split() ])
        T.append([False] * len(R[-1]))
    answer = 0
    for i, miss in enumerate(M):
        g = i/2 # game in round
        r = 0 # round
        domiss = 0
        while domiss < miss:
            domiss += 1
            g = g/2
            r = r+1
        while r < P:
            if not T[r][g]:
                answer += 1
                T[r][g] += 1
            g = g/2
            r = r+1
    #print M, R
    print "Case #%d: %d" % (case, answer)
