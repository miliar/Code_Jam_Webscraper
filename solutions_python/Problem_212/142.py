t = int(input())
for case in range(1, t + 1):
    rstr = 'Case #' + str(case) + ': '

    n, p = [int(x) for x in input().split()]
    gs = [int(x) % p for x in input().split()]
    buckets = [0] * p
    for g in gs:
        buckets[g] += 1

    res = buckets[0]
    if p == 2:
        res += (buckets[1] + 1) // 2
    elif p == 3:
        pairs = min(buckets[1], buckets[2])
        res += pairs
        remaining = max(buckets[1], buckets[2]) - pairs
        res += (remaining + 2) // 3
    elif p == 4:
        pairs = min(buckets[1], buckets[3])
        res13 = max(buckets[1], buckets[3]) - pairs
        res += pairs
        res += res13 // 4
        res13 = res13 % 4
        res += buckets[2] // 2
        res2 = buckets[2] % 2
        if res2 == 1 and res13 == 3:
            res += 2
        elif res2 > 0 or res13 > 0:
            res += 1

    rstr += str(res)

    print(rstr)
