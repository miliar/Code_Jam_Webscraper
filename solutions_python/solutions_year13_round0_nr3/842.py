def f(n):
    s = 0
    for k in [1, 4, 9, 121, 484]:
        if k <= n:
            s += 1
    return s

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print('Case #%d: %d' % (i+1, f(b) - f(a-1)))
    
