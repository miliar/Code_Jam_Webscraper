
def solve(n, k):
    assert n >= k
    if k == 1:
        m = n//2
        if n % 2 == 0:
            return m, m - 1
        else:
            return m, m
    else:
        k = k - 1 # we've split once
        n_even = n % 2 == 0
        k_even = k % 2 == 0
        if n_even and k_even:
            return solve(n//2 - 1, k//2)
        elif n_even and not k_even:
            return solve(n//2, k//2 + 1)
        elif not n_even and k_even:
            return solve(n//2, k//2)
        else:
            return solve(n//2, k//2 + 1)


def explore(n):
    for k in range(1, n+1):
        min_s, max_s = solve(n, k)
        print("{: 2d}: {} {}".format(k, max_s, min_s))

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        max_s, min_s = solve(n, k)
        print("Case #{}: {} {}".format(i, max_s, min_s))
