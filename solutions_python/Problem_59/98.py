T = int(raw_input())
for t in range(T):
    [N, M] = map(int, raw_input().split(' '))
    tree = {}
    for n in range(N):
        path = raw_input().split('/')[1:]
        nlvl = tree
        for dir in path:
            if not dir in nlvl:
                nlvl[dir] = {}
            nlvl = nlvl[dir]
    total = 0
    for m in range(M):
        path = raw_input().split('/')[1:]
        nlvl = tree
        for dir in path:
            if not dir in nlvl:
                nlvl[dir] = {}
                total += 1
            nlvl = nlvl[dir]
    print 'Case #%d: %d' % (t+1, total)

            


    