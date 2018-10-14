import sys

f = open(sys.argv[1], 'r')
T = int(f.readline().strip())

for t in xrange(1, T + 1):
    line = f.readline().split()
    s_max = int(line[0])
    S = line[1]
    
    n = 0
    pcount = 0

    for i in xrange(0, s_max + 1):
        S_i = int(S[i])
        if i > pcount + n:
            n += i - (pcount + n)
        pcount += S_i
    
    print "Case #%d: %d" % (t, n)
