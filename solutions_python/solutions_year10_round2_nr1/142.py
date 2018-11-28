
for case in range(1,int(input()) + 1):
    (N,M) = map(int, input().split())
    root = {}
    for _ in range(N):
        d = root
        for f in input()[1:].split('/'):
            if not f in d:
                d[f] = {}
            d = d[f]
    n = 0
    for _ in range(M):
        d = root
        for f in input()[1:].split('/'):
            if not f in d:
                n += 1
                d[f] = {}
            d = d[f]
    print('Case #%d: %d' % (case, n))
