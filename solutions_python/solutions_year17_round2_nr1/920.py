def solve(D, N, k_list, s_list):
    t_list = []
    for i in xrange(N):
        t_list.append((D-k_list[i])/s_list[i])

    t_list.sort()
    t_list.reverse()

    return D/t_list[0]


if True:
    T = int(raw_input())
    for i in range(1, T+1):
        #Read multiple int
        [D, N] = list(map(int, raw_input().split()))
        k_list = []
        s_list = []
        for j in xrange(N):
            [a1, a2] = list(map(float, raw_input().split()))
            k_list.append(a1)
            s_list.append(a2)
        #-------------------------------------------
        ms = solve(D, N, k_list, s_list)
        #-------------------------------------------
        print "Case #{}: {}".format(i, ms)
