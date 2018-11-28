def solve():
    n = [int(x) for x in input()]

    def decrease(n):
        if len(n) == 1:
            return n, True

        first_descent = -1
        for i in range(1, len(n)):
            if n[i] < n[i-1]:
                first_descent = i

        if first_descent == -1:
            return n, True

        n[first_descent-1] -= 1
        for i in range(first_descent, len(n)):
            n[i] = 9

        return n, False

    ok = False
    while not ok:
        n, ok = decrease(n)

    return int(''.join(map(str, n)))

T = int(input())
for t in range(T):
    print("Case #{}: {}".format(t+1, solve()))
