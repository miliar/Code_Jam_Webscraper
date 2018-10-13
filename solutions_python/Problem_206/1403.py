for tc in range(1, int(raw_input())+1):
    d, n = map(int, raw_input().split())
    horses = []
    for _ in range(n):
        horses += [map(float, raw_input().split())]
    horses.sort(key=lambda x:x[0])
    ki, si = horses[0]
    besttime = (d-ki)/si
    for kj, sj in horses[1:]:
        if sj >= si:
            continue
        t = (ki-kj)/(sj-si)
        if t*sj+kj < d:
            ki = kj
            si = sj
            besttime = (d-kj)/sj
    print "Case #%d: %f" % (tc, d/besttime)
