C = "RYB"


def main(n, l):
    for i in range(3):
        if l[i] > l[(i + 1) % 3] + l[(i + 2) % 3]:
            return 'IMPOSSIBLE'

    d = {C[i]: l[i] for i in range(3)}
    a, b, c = sorted(d, key=d.__getitem__, reverse=True)
    ans = []
    while d[a] > d[b]:
        ans += a, c
        d[a] -= 1
        d[c] -= 1
    while d[c]:
        ans += a, b, c
        d[a] -= 1
        d[b] -= 1
        d[c] -= 1
    while d[a]:
        ans += a, b
        d[a] -= 1
        d[b] -= 1
    return ''.join(ans)

for case in range(int(input())):
    n, *l = map(int, input().split())
    l = l[::2]
    ans = main(n, l)
    print("Case #%i: %s" % (case + 1, ans))
