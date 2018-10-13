import sys

input = sys.stdin
T=int(input.readline())

for i in xrange(1,T+1):
    cache = []
    cachesum = []
    R, k, N = map(int, input.readline().split())
    g = map(int, input.readline().split())
    s = 0
    curr = []
    w = 0
    cacheoff = False
    while w<R:
        # while (sum(curr) + g[0]) <= k:
        #     next = g.pop(0)
        #     curr.append(next)
        #     if len(g) == 0:
        #         break
        # g.extend(curr)
        # cachesum.append(sum(curr))
        # s += sum(curr)
        
        key = '_'.join([str(x) for x in g])
        if key not in cache or cacheoff:
            cache.append(key)
            while (sum(curr) + g[0]) <= k:
                next = g.pop(0)
                curr.append(next)
                if len(g) == 0:
                    break
            g.extend(curr)
            cachesum.append(sum(curr))
            s += sum(curr)
        else:
            o = cache.index(key)
            length = len(cache[o:])
            if length > R-w:
                cacheoff = True
                continue
            sq = sum(cachesum[o:])
            #print '-',o, length, sq
            n = (R-w)/length
            w = w+n*length-1
            #print o, key, R, w           
            s = s + n*sq
        curr = []
        w+=1
        #print w
    print "Case #%s: %s" % (i, s)
    #print cache
