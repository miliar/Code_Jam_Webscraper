def solve():
    n, r, o, y, g, b, v = map(int, raw_input().split())
    cant = "IMPOSSIBLE"
    if r + y + b == 0 or r < g or y < v or b < o:
        return cant
    if y + b == 0:
        if r == g:
            return "RG" * r
        else:
            return cant
    if r + b == 0:
        if y == v:
            return "YV" * y
        else:
            return cant
    if r + y == 0:
        if b == o:
            return "BO" * b
        else:
            return cant
    if r <= g - 1 or y <= v - 1 or b <= o - 1:
        return cant
    r -= g
    y -= v
    b -= o
    tb = [[r, "R"], [y, "Y"], [b, "B"]]
    tb.sort(reverse=True)
    if tb[0][0] > tb[1][0] + tb[2][0]:
        return cant
    dif = tb[1][0] - tb[2][0]
    ans = [tb[0][1], tb[1][1]] * dif
    tb[0][0] -= dif
    tb[1][0] -= dif
    p = ""
    sw = 1
    for i in xrange(tb[1][0] + tb[2][0]):
        if tb[0][0]:
            tb[0][0] -= 1
            ans.append(tb[0][1])
        ans.append(tb[sw][1])
        sw = 3 - sw
    for c, cc, k in [["R", "G", g], ["Y", "V", v], ["B", "O", o]]:
        for i in xrange(len(ans)):
            if ans[i] == c:
                ans[i] = c + (cc + c) * k
                break
    return "".join(ans)


T = int(raw_input())
for t in xrange(T):
    print "Case #%d: %s" % (t + 1, solve())
