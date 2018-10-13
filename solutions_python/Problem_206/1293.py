import math


def solve():
    f = open("A-large.in", "r")
    T = int(f.readline())
    out = open("output.out", "w")

    for case in range(T):
        D, N = map(int, f.readline().split())
        ans = -1

        for i in range(N):
            k, s = map(int, f.readline().split())
            ans = max((D - k) / s, ans)


        print('Case #%d: %f' % (case + 1, D / ans))
        out.write('Case #%d: %f\n' % (case + 1, D / ans))

solve()
