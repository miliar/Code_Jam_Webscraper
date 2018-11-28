T = int(raw_input())

for x in xrange(1, T+1):
    N, K = raw_input().split(" ")
    N, K = int(N), int(K)
    s1 = s2 = 0  # Side 1 and 2
    ess_dict = {N: 1}  # Empty stalls sets
    ess_lst = [N]
    while K > 0:
        cur_ess = ess_lst[-1]  # Current empty stall set
        ess_dict[cur_ess] -= 1
        if cur_ess == 1:
            s1 = s2 = 0
        elif cur_ess == 2:
            s1, s2 = 0, 1
        else:
            if cur_ess % 2 == 0:
                s1 = (cur_ess / 2) - 1
            else:
                s1 = cur_ess / 2
            s2 = cur_ess / 2

        if s1 != 0:
            ess_dict[s1] = ess_dict.get(s1, 0) + 1
            if s1 not in ess_lst:
                ess_lst.insert(0, s1)
        if s2 != 0:
            ess_dict[s2] = ess_dict.get(s2, 0) + 1
            if s2 not in ess_lst:
                ess_lst.insert(0, s2)

        if ess_dict[cur_ess] == 0:
            del ess_dict[cur_ess]
            ess_lst.remove(cur_ess)
            ess_lst.sort()
        K -= 1

    print "Case #{}: {} {}".format(x, max(s1, s2), min(s1, s2))
