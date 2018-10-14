T = int(raw_input())
for t in range(1, T+1):
    n, k = map(int, raw_input().split())
    k %= 2 ** n
    mask = 2 ** n - 1
    on = mask == k
    ans = "ON" if on else "OFF"
    print "Case #%d: %s" % (t, ans)
