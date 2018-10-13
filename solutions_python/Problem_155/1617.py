for _ in range(int(input())):
    k = 0
    m, p = input().split()
    p = list(map(int, p))
    # print("Case #{}: ".format(_ + 1) + str(p.count(0)))
    for i in range(1, len(p)):
        while sum(p[0:i]) < i:
            p[i - 1] += 1
            k += 1
    print("Case #{}:".format(_ + 1), k)
