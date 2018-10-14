# Andy Rock
# April 14, 2017
# 
# Round 1A 2017: Problem A. 

for T in xrange(1, int(raw_input()) + 1):

    R, C = map(int, raw_input().split())
    cake = [[c for c in raw_input()] for _ in xrange(R)]

    for i in xrange(R):
        for j in xrange(C):
            if cake[i][j] != '?':
                for k in xrange(j + 1, C):
                    if cake[i][k] == '?':
                        cake[i][k] = cake[i][j]
                    else:
                        break
                for k in xrange(j - 1, -1, -1):
                    if cake[i][k] == '?':
                        cake[i][k] = cake[i][j]
                    else:
                        break

    for a in xrange(2):
        for i in xrange(1, R):
            for j in xrange(C):
                if cake[i][j] == '?' and cake[i - 1][j] != '?':
                    k = j + 1
                    while k < C:
                        if cake[i][k] != '?' or cake[i - 1][k] != cake[i - 1][j]:
                            break
                        k += 1
                    for l in xrange(j, k):
                        cake[i][l] = cake[i - 1][j]
        cake = cake[::-1]

    print 'Case #%d:' % T
    print '\n'.join(''.join(c) for c in cake)
