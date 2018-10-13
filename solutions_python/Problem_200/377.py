from functools import reduce

def solve(n):
    d = [int(x) for x in n]
    l = len(d)
    i = 1
    while i < l and d[i - 1] <= d[i]:
        i += 1
    if i == l:
        return d
    for j in range(i, len(d)):
        d[j] = 9
    for k in range(i - 1, 0, -1):
        if d[k] > d[k - 1]:
            d[k] -= 1
            return d
        d[k] = 9
    d[0] -= 1
    return d
        
t = int(input())
for i in range(t):
    d = solve(input())
    result = reduce(lambda x, y: x * 10 + y, d, 0)
    print('Case #%d: %d' % (i + 1, result))