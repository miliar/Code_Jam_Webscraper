def f(n, m):
    if n<10:
        return min(n, m)

    l = n%10
    d = min(l, m)
    x = f(n//10, d)
    r1 = d + x*10

    if n%10!=m:
        while n%10!=m:
            n -= 1
        d = m
        x = f(n//10, d)
        r2 = d + x*10

        r1 = max(r1, r2)

    return r1

for t in range(int(input())):
    n = int(input())

    ans = f(n, 9)
    print('Case #{}: {}'.format(t+1, ans))