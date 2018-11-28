data = iter(open("C-small-1-attempt0.in").read().splitlines())
T = int(next(data))
for caseNum in range(1, T + 1):
    n,k = map(int, next(data).split())
    u = float(next(data))
    p = sorted(map(float, next(data).split()))[-k:]
    ans = 0
    for i in range(len(p)):
        ss = p[:i+1]
        s = sum(ss)
        avg = (s + u)/len(ss)
        #print ss, avg
        if avg >= ss[-1]:
            zz = avg**len(ss)
            for j in p[i+1:]:
                zz *= j
            #print zz
            new_ans = zz
            ans = max(ans, new_ans)
    print "Case #%d: %s" % (caseNum, ans)