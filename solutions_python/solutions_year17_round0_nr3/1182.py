    
def solve(n, k):
    i = 0
    while 2 ** i <= k:
        i += 1
    number = k - (2 ** (i - 1)) + 1 
    can = n // (2 ** i)
    a = n - (2 ** i) + 1 - (2 * can - 1) * (2 ** (i - 1))
    b = 2 ** (i - 1) - a
    if a >= 0 and b >= 0:
        if a >= number:
            res_max = can
            res_min = can
            return res_max, res_min
        else:
            res_max = can
            res_min = can - 1
            return res_max, res_min
    else:
        a = n - (2 ** i) + 1 - (2 * can - 2) * (2 ** (i - 1))
        b = 2 ** (i - 1) - a
        if a >= 0 and b >= 0:
            if a >= number:
                res_max = can
                res_min = can - 1
                return res_max, res_min
            else:
                res_max = can - 1
                res_min = can - 1
                return res_max, res_min


tests = int(input())
for test in range(tests):
    n, k = [int(x) for x in input().split()]
    res_max, res_min = solve(n, k)
    print("Case #%d:" % (test + 1), res_max, res_min)
