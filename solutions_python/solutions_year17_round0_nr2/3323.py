import math


def solve():
    f = open("B-small-attempt1.in", "r")
    T = int(f.readline())
    out = open("output.out", "w")

    for case in range(T):
        N = int(f.readline())
        ans = 0
        if N < 10:
            ans = N
        ok = True
        digits = int(math.log10(N)) + 1
        for x in range(digits, 1, -1):
            if (N % 10 ** x) // 10 ** (x - 1) > (N % 10 ** (x - 1)) // 10 ** (x - 2):
                ok = False
                break
        if ok:
            ans = N
        else:
            for x in range(digits, 1, -1):
                if (N % 10 ** x) / 10 ** (x - 1) > (N % 10 ** (x - 1)) / 10 ** (x - 2):
                    ans = N - ( (N % 10 ** (x - 1)) + 1)
                    break
        print('Case #%d: %d' % (case + 1, ans))
        out.write('Case #%d: %d\n' % (case + 1, ans))

solve()
