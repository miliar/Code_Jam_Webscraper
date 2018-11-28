import sys, os

fin = open(sys.argv[1], 'r')

C = int(fin.readline())
for i in range(0, C):
    N = int(fin.readline().strip())
    pairs = []
    for j in range(0, N):
        inp = fin.readline().strip().split(' ')
        pairs.append((int(inp[0]), int(inp[1])))
    #print >> sys.stderr, pairs
    cnt = 0
    for j in range(0, N-1):
        for k in range(j + 1, N):
            #print >> sys.stderr, pairs[j], pairs[k]
            if (pairs[j][0] < pairs[k][0] and pairs[j][1] > pairs[k][1]) or \
                    (pairs[j][0] > pairs[k][0] and pairs[j][1] < pairs[k][1]):
                cnt = cnt + 1
    print 'Case #%i:' % (i + 1), cnt
