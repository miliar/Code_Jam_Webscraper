
def solve():
    v = raw_input().split();
    [n, m] = map(int, v)
    mp = set()
    mp.add("/")
    for x in range(n):
        path = raw_input()
        comp = path.split("/")
        now = ""
        for y in comp:
            now = now + "/" + y
            mp.add(now)

    ans = 0

    for x in range(m):
        path = raw_input()
        comp = path.split("/")
        now = ""
        for y in comp:
            now = now + "/" + y
            if now not in mp:
                ans = ans + 1
                mp.add(now)
    return ans

nC = int(raw_input())
for nc in xrange(1, nC+1):
    print "Case #%d: %d" %(nc, solve())


