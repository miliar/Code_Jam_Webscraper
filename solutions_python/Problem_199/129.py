from collections import deque

t = int(input())

for i in range(t):
    s, k = input().split()
    q = deque()
    cnt = total = 0
    k = int(k)
    s = list(s)
    for z in s:
        b = z != '+'
        b ^= cnt & 1
        q += [b]
        cnt += b
        total += b
        if len(q) >= k:
            cnt -= q.popleft()

    print("Case #%d: " % (i + 1),end='')
    if cnt:
        print('IMPOSSIBLE')
    else:
        print(total)
