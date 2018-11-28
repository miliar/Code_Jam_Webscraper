import sys

fin = sys.stdin
C = int(fin.readline())

for c in xrange(1, C + 1):
    N, K, B, T = map(int, fin.readline().split())

    X = map(int, fin.readline().split())[::-1]
    V = map(int, fin.readline().split())[::-1]

    got = 0
    slows = 0
    swaps = 0

    for i, x in enumerate(X):
        if got == K:
            break
        if V[i] * T + x >= B:
            got += 1
            #need to pass all slows
            swaps += slows
        else:
            #wont make it, too slow!
            slows += 1

    print 'Case #' + str(c) + ':',
    if got == K:
        print swaps
    else:
        print 'IMPOSSIBLE'
