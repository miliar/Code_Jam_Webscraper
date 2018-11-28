for case in range(int(input())):
    s_max, s_arry = input().split()
    n_friend, n_stand = 0, int(s_arry[0])
    for i, pivot in enumerate(s_arry[1:]):
        n_need = (i - n_stand + 1) if (i+1 > n_stand) else 0
        n_friend += n_need
        n_stand  += (n_need + int(pivot))
    print ('Case #{}: {}'.format(case+1, n_friend))
