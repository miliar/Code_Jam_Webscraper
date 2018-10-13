t = int(input())
for test_case in range(1, t+1):
    N, K = [int(x) for x in input().split()]
    U = float(input())
    ps = sorted([float(x) for x in input().split()]) + [1]
    # print()
    # print(ps, U)
    for i in range(1, len(ps)):
        next_difference = ps[i] - ps[i-1]
        if i * next_difference <= U:
            U -= i * next_difference
            ps = [ps[i]] * i + ps[i:]
        else:
            improve = U / i
            U -= i * improve
            ps = [ps[0] + improve] * i + ps[i:]
            break
        # print(ps, U)
    res = 1
    for p in ps:
        res *= p
    
    print("Case #{}: {}".format(test_case, res))
