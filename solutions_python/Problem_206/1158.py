"""https://code.google.com/codejam/contest/8294486/dashboard"""

if __name__ == '__main__':
    t = int(input())
    get = lambda: list(map(int, input().split()))
    for case in range(1, t + 1):
        D, N = get()
        max_time = max( (D - k)/ s for k, s in [get() for _ in range(N)])
        res = D / max_time
        print("Case #{}: {}".format(case, res))
