def solve(n):
    for i in range(len(n) - 2, -1, -1):
        if n[i] > n[i + 1]:
            n[i] -= 1
            if n[i] < 0:
                n[i-1] -= 1
            for j in range(i+1, len(n)):
                n[j] = 9
    return int("".join(map(str, n)))

t = int(raw_input())

for i in range(1, t + 1):
    n = map(int, list(raw_input().strip()))
    print("Case #%d: %d" % (i, solve(n)))
