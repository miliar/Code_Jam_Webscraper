def count_ring(r, t):
    n = 0
    while (1):
        area = 2 * r + 2 * (n * 2) + 1
        if t < area:
            break
        n += 1
        t -= area
    return n

def count_ring2(r, t):
    n = 0
    a = 2 * r - 1
    while (2 * n + a) * n <= t:
        n += 1
    return n - 1

for i in range(int(raw_input())):
    r, t = map(int, raw_input().split())
    print 'Case #{}: {}'.format(i + 1, count_ring2(r, t))

