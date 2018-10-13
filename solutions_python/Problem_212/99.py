tests = int(input())


def solve():
    n, p = map(int, input().split())
    a = [int(x) % p for x in input().split()]
    freq = [0, 0, 0, 0]
    for x in a:
        freq[x] += 1
    res = freq[0]

    if p == 2:
        res += (freq[1] - 1) // 2 + 1
    elif p == 3:
        smaller = min(freq[1], freq[2])
        res += smaller
        rem = max(freq[1], freq[2]) - smaller
        res += (rem - 1) // 3 + 1

    elif p == 4:
        smaller = min(freq[1], freq[3])
        res += smaller
        res += freq[2] // 2
        rem = max(freq[1], freq[3]) - smaller
        if freq[2] % 2 == 0:
            res += (rem - 1) // 4 + 1
        else:
            res += (rem + 2 - 1) // 4 + 1

    return res

for ti in range(1, tests + 1):
    print("Case #{}: {}".format(ti, solve()))
