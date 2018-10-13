from collections import deque

spl = lambda x: (x - x // 2, x // 2)

t = int(input())
for x in range(t):
    n, k = map(int, input().split())
    dct = {n: 1}
    q = deque()
    q += [n]
    print("Case #%d: " % (x + 1), end='')
    while 1:
        sz = q.popleft()
        cnt = dct.pop(sz)
        k -= cnt
        s = spl(sz - 1)
        if k <= 0:
            print("%d %d" % s)
            break
        if s[0] in dct:
            dct[s[0]] += cnt
        else:
            q += [s[0]]
            dct[s[0]] = cnt
        if s[1] in dct:
            dct[s[1]] += cnt
        else:
            q += [s[1]]
            dct[s[1]] = cnt
