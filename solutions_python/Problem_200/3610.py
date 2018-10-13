def ok(n):
    res = True
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return i
    return -1


def main():
    n = list(map(int, list(input())))
    i = ok(n)
    while i != -1:
        n[i] -= 1
        for k in range(i + 1, len(n)):
            n[k] = 9
        i = ok(n)
    print(int("".join(list(map(str, n)))))




T = int(input())
for t in range(1, T + 1):
    print("Case #%d: " % t, end="")
    main()