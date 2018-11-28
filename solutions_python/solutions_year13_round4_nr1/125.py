import sys

def cost(N, di):
    return di * N - di * (di - 1) / 2

T = int(raw_input())
for i in xrange(1, T + 1):
    N, M = map(int, raw_input().split())
    pos = set()
    param = []
    for j in xrange(M):
        o, e, p = map(int, raw_input().split())
        param.append((o, e, p))
        pos.add(o)
        pos.add(e)
    key = list(pos)
    key.sort()
    
    mapping = {}
    rev_map = {}
    c = 0
    for k in key:
        if k not in mapping:
            mapping[k] = c * 2
            rev_map[c * 2] = k
            c += 1
    
    c *= 2
    check = [0] * c
    total = 0
    for o, e, p in param:
#        print o, e, p, p * cost(N, e - o)
#        print mapping[o], mapping[e], p
        total += p * cost(N, e - o)
        for d in xrange(mapping[o], mapping[e] + 1):
            check[d] += p
#    print 'total: ', total
    reduc = 0
    while True:
        length = 0
        temp_o = 0
        temp_e = 0
        size = 0
        for d in xrange(c):
            if check[d] <= 0:
                continue
            if d not in rev_map:
                continue
            start = rev_map[d]
            for e in xrange(d, c):
                if check[e] <= 0:
                    break
                if e not in rev_map:
                    continue
                end = rev_map[e]
                if end - start > length:
                    length = end - start
                    temp_o = d
                    temp_e = e
#        print length, temp_o, temp_e, check[temp_o:temp_e+1]
        if length == 0:
            break
        else:
            mind = min(check[temp_o:temp_e+1])
            reduc += mind * cost(N, length)
#            print 'reduc: ', mind * cost(N, length), length
            for d in xrange(temp_o, temp_e + 1):
                check[d] -= mind
#        for d in xrange(c):
#            print check[d],
#        print
    
    print "Case #{0}: {1}".format(i, total - reduc)

