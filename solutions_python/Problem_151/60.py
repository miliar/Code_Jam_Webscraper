maxnode = -1
maxnodecase = 0
buf = [0] * 100


def bt(lev, s, M, N):
    if lev == M:
        global maxnode, maxnodecase
        if len(set(buf[:M])) != N:
            return

        cnt = N
        trie = [{} for i in xrange(N)]

        for index, st in enumerate(s):
            cur = trie[buf[index]]
            for ch in st:
                if ch not in cur:
                    cnt += 1
                    cur[ch] = {}
                cur = cur[ch]

        if cnt > maxnode:
            maxnode = cnt
            maxnodecase = 1
        elif cnt == maxnode:
            maxnodecase += 1
    else:
        for j in xrange(N):
            buf[lev] = j
            bt(lev+1, s, M, N)


for tc in range(input()):

    maxnode = -1
    maxnodecase = 0

    M, N = map(int, raw_input().split())
    s = []

    for i in range(M):
        s.append(raw_input().strip())

    bt(0, s, M, N)

    print 'Case #%d:' % (tc+1), maxnode, maxnodecase
