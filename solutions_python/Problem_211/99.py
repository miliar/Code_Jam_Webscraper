T = int(input())
for case in range(1, T+1):
    n, k = map(int, input().split())
    u = float(input())
    ps = list(sorted(map(float, input().split())))
    # print(ps)
    num = 1
    for i in range(len(ps)-1):
        if num*(ps[i+1] - ps[i]) > u:
            break
        else:
            u -= num*(ps[i+1] - ps[i])
            for j in range(i+1):
                ps[j] = ps[i+1]
        num += 1
    for i in range(num):
        ps[i] += u/(num)
    # print(ps)
    result = 1.
    for p in ps:
        result *= p
    result = min(1, result)
    print(f"Case #{case}: {result:.10f}")
