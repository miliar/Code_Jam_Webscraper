n = input()
for roundi in range(n):
    se = {}
    s = input()
    for i in range(s):
        se[raw_input()]=i
    q = input()
    items = []
    for i in range(q):
        items.append(se[raw_input()])

    cache = []
    for i in range(q):
        inner = []
        for j in range(s):
            inner.append(0)
        cache.append(inner)

    for roundn in range(q-1,-1,-1):
        if roundn < q-1:
            for i in range(s):
                if cache[roundn+1][i] != q+2:
                    cache[roundn][i] = cache[roundn+1][i]
                else:
                    cache[roundn][i] = min(cache[roundn+1])+1
        cache[roundn][items[roundn]] = q+2

    try:
        print "Case #%d: %d" % (roundi+1, min(cache[0]))
    except:
        print "Case #%d: 0" % (roundi+1,)
