def calculate_min_max(s):

    cur_min = -1
    indices = []
    min_vals = []
    max_vals = []

    ret_min = ret_max = -1
    more_than_one_min = False
    for idx in s:
        l = r = 0
        l_idx = r_idx = idx
        while l_idx-1 in s:
            l += 1
            l_idx -= 1
        while r_idx+1 in s:
            r += 1
            r_idx += 1

        min_lr = min(l,r)
        max_lr = max(l,r)

        if min_lr > cur_min:
            cur_min = min_lr
            indices = [ idx ]
            min_vals = [ cur_min ]
            max_vals = [ max_lr ]
            more_than_one_min = False
        elif min_lr == cur_min:
            indices.append(idx)
            min_vals.append(min_lr)
            max_vals.append(max_lr)
            more_than_one_min = True

    ptr = 0
    if more_than_one_min:
        max_max_val = max(max_vals)
        ptr = max_vals.index(max_max_val)

    chosen_idx = indices[ptr]
    min_val = min_vals[ptr]
    max_val = max_vals[ptr]

    return chosen_idx, max_val, min_val


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # 1 <= N <= 10^18
    N, K = map(int, input().split())


    empty_stalls = set(range(1,N+1)) # From 1 to N
    # 0 | 1 | 2 | 3 | 4 | ... | N | N+1
    #bathrooms = [1] + [0] * N + [1] # List of 0s and 1s to indicate occupied/vacancy

    for user in range(K):
        #print()
        #print('user: {}'.format(user))
        # Loop from empty_stalls
        idx, max_val, min_val = calculate_min_max(empty_stalls)
        #print("stalls: {}".format(list(empty_stalls)))
        #print('idx: {}'.format(idx))
        empty_stalls.remove(idx)

    print("Case #{}: {} {}".format(i, max_val, min_val ))
