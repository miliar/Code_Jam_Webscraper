c = int(raw_input())
for case in range(1, c+1):
    g = map(int,raw_input().split())
    l = g.pop(0)
    t = g.pop(0)
    n = g.pop(0)
    c = g.pop(0)

    mp = [g[i%c]*2 for i in range(n)]
    time = t
    for i in range(n):
        if time == 0:
            break
        elif time>=mp[i]:
            time -= mp[i]
            mp[i] = 0
        else:
            temp = mp[i]
            mp[i] -= time
            time = 0
    mp.sort()
    mp.reverse()
    for i in range(n):
        if l==0:
            break
        mp[i] /= 2
        l -= 1
    total = t - time + sum(mp)
    print "Case #%d: %d" % (case, total)
