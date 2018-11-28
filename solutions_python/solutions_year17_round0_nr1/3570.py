def flips(a, M, N):
    sum = res = 0
    s = [0] * M
    for i in range(0, M):
        s[i] = (int(a[i]) + sum) % 2 != 1
        sum += s[i] - (s[i- N + 1] if (i >= N - 1) else 0)
        res += s[i]
        if i > M - N and s[i] != 0:
            return float('inf')
    return res

def main():
    with open('A-large.in.txt') as f:
        n = int(f.readline())
        for i in range(0, n):
            (s, k) = f.readline().split(" ")
            s = map(int, list(s.replace("-", "0").replace("+", "1")))
            res = flips(s, len(s), int(k))
            print("Case #%s: %s" % (i + 1, ('IMPOSSIBLE' if res == float('inf') else res)))

main()
# input = map(int, list("00010110"))
# print(flips(input, 8, 3))

# input = map(int, list("111111"))
# print(flips(input, 6, 4))


# input = map(int, list("01010"))
# print(flips(input, 5, 4))


