
def solve(t):
    N, P = map(int, raw_input().split())
    G = map(int, raw_input().split())
    if P == 2:
        ans = N - sum([g % 2 for g in G]) / 2
    elif P == 3:
        G = [g % 3 for g in G]
        cnt1 = G.count(1)
        cnt2 = G.count(2)
        cnt1, cnt2 = min(cnt1, cnt2), max(cnt1, cnt2)
        tmp = cnt1
        for i in xrange(cnt2 - cnt1):
            tmp += i % 3 != 0
        ans = N - tmp
    elif P == 4:
        G = [4 - g % 4 for g in G]
        cnt1 = G.count(1)
        cnt2 = G.count(2)
        cnt3 = G.count(3)
        cnt1, cnt3 = min(cnt1, cnt3), max(cnt1, cnt3)
        tmp = cnt1 + cnt2 / 2
        cnt2 %= 2

        tmp2 = cnt2 * 2
        for i in xrange(cnt3 - cnt1):
            if tmp2 % 4 != 0:
                tmp += 1
            tmp2 += 1
        ans = N - tmp


    print "Case #%d: %d" % (t, ans)

T = int(raw_input())
for t in xrange(T):
    solve(t+1)
