t = int(raw_input().strip())

for i in range(t):
    n = int(raw_input().strip())
    nw = sorted(map(float, raw_input().strip().split(' ')))
    kw = sorted(map(float, raw_input().strip().split(' ')))
    naomiOpt = 0
    naomiBad = n
    index = 0
    for u in range(n):
        if nw[u] > kw[index]:
            naomiOpt += 1
            index += 1
    index = 0
    for u in range(n):
        if kw[u] > nw[index]:
            naomiBad -= 1
            index += 1

    print "Case #%d: %d %d" % (i + 1, naomiOpt, naomiBad)

