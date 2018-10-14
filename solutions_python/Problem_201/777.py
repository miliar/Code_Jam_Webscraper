t = int(input())

for test in range(1, t+1):
    n, k = map(int, input().split())
    a, b = 1, 0

    i = 0
    while k > 2 ** i:
        if n % 2 == 1:
            a = 2 * a + b
        else:
            b = 2 * b + a
        n //= 2
        k -= 2 ** i
        i += 1

    if k > a:
        n -= 1
    ans = (n // 2, n // 2) if n % 2 == 1 else (n // 2, n // 2 - 1)

    print('Case #%d: %d %d' % (test, *ans))
