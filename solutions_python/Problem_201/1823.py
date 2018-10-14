from sortedcontainers import SortedList  # http://www.grantjenks.com/docs/sortedcontainers/

for case in range(int(input())):
    N, K = map(int, input().split())
    lst = SortedList([N])

    for _ in range(K-1):
        s = lst.pop()
        l, r = s // 2, (s-1) // 2
        if l != 0:
            lst.add(l)
        if r != 0:
            lst.add(r)

    s = lst.pop()
    l, r = s // 2, (s-1) // 2
    ans1 = max(l, r)
    ans2 = min(l, r)

    print('Case #%d: %s %s' % (case+1, ans1, ans2))
