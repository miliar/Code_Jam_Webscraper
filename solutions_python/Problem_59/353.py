t = int(raw_input())
for c in range(1,t+1):
    dirs = { }

    n,m = [int(i) for i in raw_input().split(' ')]
    count = 0

    for i in range(n):
        cdir = dirs
        r = raw_input()
        r = r.split('/')[1:]
        for d in r:
            if not cdir.has_key(d):
                cdir[d] = {}
            cdir = cdir[d]

    for i in range(m):
        cdir = dirs
        r = raw_input()
        r = r.split('/')[1:]
        for d in r:
            if not cdir.has_key(d):
                cdir[d] = {}
                count += 1
            cdir = cdir[d]
    print "Case #%d: %d"%(c, count)
