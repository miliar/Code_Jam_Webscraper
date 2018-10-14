from itertools import product

surprising = {}
not_surprising = {}

for p in product(range(0,11), range(0, 11), range(0,11)):
    p = tuple(sorted(list(p)))
    if max(p)-min(p) > 2:
        continue
    target = not_surprising
    if max(p)-min(p) == 2:
        target = surprising
    target[sum(p)] = max(p)

T = int(raw_input())

for case in xrange(1, T+1):
    tokens = map(int, raw_input().split())
    N, S, p = tokens[:3]
    t = tokens[3:]
    t.sort(reverse=True)

    ans = 0
    newt = []
    for v in t:
        if v not in not_surprising:
            S -= 1
            if surprising[v] >= p:
                ans += 1
        else:
            newt.append(v)

    t = newt

    for v in t:
        if not_surprising[v] >= p:
            ans += 1
        elif v in surprising and surprising[v] >= p and S > 0:
            ans += 1
            S -= 1

    print "Case #%d: %d"%(case, ans)
