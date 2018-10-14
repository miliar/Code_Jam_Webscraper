T = int(input())
lines = []
for _ in range(T):
    lines.append(input())

for case, line in enumerate(lines):
    N = list(map(lambda c: int(c), line))[::-1]
    i = 0
    length = len(N)
    while i < length - 1:
        if N[i] < N[i + 1]:
            N[i] = 9
            N[i + 1] -= 1
            for j in range(i):
                N[j] = 9
        i += 1
    N = int("".join(map(lambda x: str(x), N[::-1])))
    print("Case #{}: {}".format(case + 1, N))
