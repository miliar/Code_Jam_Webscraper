T = int(raw_input())
for t in range(T):
    N, M = [int(s) for s in raw_input().split()]
    tree = {}
    for i in range(N):
        dirs = raw_input().split('/')[1:]
        p = tree
        for dir in dirs:
            if dir not in p:
                p[dir] = {}
            p = p[dir]
    total = 0
    for j in range(M):
        dirs = raw_input().split('/')[1:]
        p = tree
        for dir in dirs:
            if dir not in p:
                p[dir] = {}
                total += 1
            p = p[dir]
    print 'Case #{0}: {1}'.format(t + 1, total)
