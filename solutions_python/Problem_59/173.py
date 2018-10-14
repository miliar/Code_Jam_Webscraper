def insert(root, path):
    if not path:
        return 0
    x = path[0]
    y = path[1:]
    if x in root:
        return insert(root[x], y)
    else:
        root[x] = {}
        return 1 + insert(root[x], y)

T = int(raw_input())
for t in range(1, T + 1):
    N, M = map(int, raw_input().split())
    root = {}
    for n in range(N):
        insert(root, raw_input().split('/')[1:])
    ans = sum(insert(root, raw_input().split('/')[1:]) for m in range(M))
    print "Case #%d: %d" % (t, ans)
        
