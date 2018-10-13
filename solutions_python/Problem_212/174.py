from collections import defaultdict

if __name__ == "__main__":
    cases = int(input())
    for case in range(1, cases+1):
        n, p = map(int, input().split(' '))
        groups = list(map(int, input().split(' ')))
        ans = 0

        d = defaultdict(int)

        for i in groups:
            d[i % p] += 1

        # put i % p == 0 first
        ans += d[0]

        if p == 2:
            ans += d[1] // 2
            if d[1] % 2 == 1:
                ans += 1

        elif p == 3:
            ones_and_twos = min(d[1], d[2])
            d[1] -= ones_and_twos
            d[2] -= ones_and_twos
            ans += ones_and_twos

            ans += (d[1] + d[2]) // 3
            if (d[1] + d[2]) % 3 > 0:
                ans += 1

        elif p == 4:
            ans += d[2] // 2
            d[2] %= 2

            ones_and_threes = min(d[1], d[3])
            d[1] -= ones_and_threes
            d[3] -= ones_and_threes
            ans += ones_and_threes

            if d[2] == 0:
                ans += (d[1] + d[3]) // 4
                if (d[1] + d[3]) % 4 > 0:
                    ans += 1

            else:
                if d[1] >= 2:
                    d[1] -= 2
                    d[2] -= 1
                    ans += 1
                elif d[3] >= 2:
                    d[3] -= 2
                    d[2] -= 1
                    ans += 1

                ans += (d[1] + d[3]) // 4
                if (d[1] + d[3] + d[2]) % 4 > 0:
                    ans += 1

        print("Case #{}: {}".format(case, ans))
