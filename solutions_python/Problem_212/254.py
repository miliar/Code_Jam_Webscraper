ints = lambda: map(int, input().split())


def work():
    n, p = ints()
    cnt = [0] * p
    for x in ints():
        cnt[x % p] += 1

    if p == 2:
        return cnt[0] + (cnt[1] + 1) // 2

    if p == 3:
        a = min(cnt[1], cnt[2])
        b = (max(cnt[1], cnt[2]) - a + 2) // 3
        return cnt[0] + a + b

    if p == 4:
        a = min(cnt[1], cnt[3])
        b = max(cnt[1], cnt[3]) - a
        c = b // 4
        d = b % 4
        e = cnt[2] // 2
        f = cnt[2] % 2
        g = 1 if (d + 2 * f > 4) else 0
        return cnt[0] + a + c + e + g


for i in range(int(input())):
    print('Case #{}: {}'.format(i + 1, work()))
