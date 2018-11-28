def solve(n, k):
    log = 0
    k4 = k
    while k4:
        k4 >>= 1
        log += 1
    k2 = 1 << (log - 1)
    base_val, plus_count = divmod(n - k2 + 1, k2)
    sz = base_val + (k - k2 + 1 <= plus_count)
    return sz // 2, (sz - 1) // 2

for i in range(1, int(input()) + 1):
    print("Case #", i, ": ", ' '.join(map(str, solve(*map(int, input().split())))), sep='')

