N = input()
for c in range(1, N+1):
    size = input()
    cand = sorted(map(int, raw_input().split()))
    d_count = [ 0  for _ in range(20)]
    for cd in cand:
        for d in range(19, -1, -1):
            if (cd>>d)&1: d_count[d] += 1
    isNo = False
    for d in range(20):
        if d_count[d]%2!=0:
            isNo = True; break
    res = "NO" if isNo else sum(cand[1:])
    print "Case #%d: %s" % (c, res)
