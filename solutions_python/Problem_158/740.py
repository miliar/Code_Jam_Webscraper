d = [
    None,
    [None,[1],[1,2],[1],[1,2]],
    [None,None,[1,2],[1,2,3],[1,2]],
    [None,None,None,[1,3],[1,2,3,4]],
    [None,None,None,None,[1,2,4]],
]
cases = input()
for case in range(1, cases + 1):
    x, r, c = map(int, raw_input().split())
    if r > c:
        r, c = c, r
    ans = "GABRIEL" if x in d[r][c] else "RICHARD"
    print "Case #%d: %s" % (case, ans)


