import collections

tc = int(input())

for t in range(tc):
    s, k = input().split()
    k = int(k)
    
    q = collections.deque()

    res = 0
    for i in range(len(s) - k + 1):
        if len(q) > 0 and q[0] == i:
            q.popleft()
        if ((1 if s[i] == '+' else 0) + len(q)) % 2 == 0:
            q.append(i + k)
            res += 1

    for i in range(len(s) - k + 1, len(s)):
        if len(q) > 0 and q[0] == i:
            q.popleft()
        if ((1 if s[i] == '+' else 0) + len(q)) % 2 == 0:
            print("Case #%d: IMPOSSIBLE" % (t+1))
            break
    else:
        print("Case #%d: %d" % (t+1, res))
        
