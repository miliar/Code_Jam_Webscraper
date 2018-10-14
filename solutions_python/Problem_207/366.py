f = open('in', 'r')
fout = open('out', 'w')
t = int(f.readline())
from heapq import heappush
from heapq import heappop

for casenum in range(1, t + 1):
    print casenum
    n, r, o, y, g, b, v = f.readline().split()
    n = int(n)
    r = int(r)
    o = int(o)
    y = int(y)
    g = int(g)
    b = int(b)
    v = int(v)

    # r, y, b
    # r y = o
    # y b = g
    # r b = v

    tot = n
    if r > tot/2 or y > tot/2 or b > tot/2:
        ans = "IMPOSSIBLE"
    else:
        # h = []
        ans = ''
        # heappush(h, (-r, 'R'))
        # heappush(h, (-y, 'Y'))
        # heappush(h, (-b, 'B'))
        dcount = {
            'B': b,
            'Y': y,
            'R': r,
        }
        d = {
            'B' : 2000,
            'Y' : 2000,
            'R' : 2000,
        }
        cur = 0
        if dcount['R'] > dcount['B']:
            last = 'R'
        else:
            last = 'B'

        if dcount[last] < dcount['Y']:
            last = 'Y'
        ans += last
        dcount[last] -= 1
        tot -= 1
        d[last] = cur
        cur += 1
        next = {
            'B': ('Y', 'R'),
            'Y': ('B', 'R'),
            'R': ('Y', 'B'),
        }
        while tot:
            v1, v2 = next[last]
            if dcount[v1] > dcount[v2]:
                last = v1
            else:
                last = v2
            dcount[last] -= 1
            ans += last
            d[last] = cur
            cur += 1
            # v = heappop(h)
            # ans += v[1]
            # d[v[1]] = cur
            # cur += 1
            # heappush(h, (v[0]+1, v[1]))
            tot -= 1



        kecil = min(d['R'], d['Y'])
        kecil = min(kecil, d['B'])
        if ans[kecil] == ans[-1]:
            kecil -= 1

        while ans[0] == ans[-1]:
            first = ans[:kecil]
            second = ans[kecil+1:]
            ans = first + second + ans[kecil]
    # print ans
    # if ans == "IMPOSSIBLE":
    #     continue
    # cur = ans[0]
    # for i in range(len(ans[1:])):
    #     k = ans[i+1]
    #     if k == cur:
    #         print "EDRROR", i
    #     cur = k
    # if ans[-1] == ans[0]:
    #     print "GGWP"
    fout.write("Case #{}: {}\n".format(casenum, ans))