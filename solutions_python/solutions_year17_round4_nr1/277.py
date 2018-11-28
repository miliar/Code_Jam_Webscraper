
T = int(input())
for t in range(1, T+1):
    N, P = [int(x) for x in input().split(' ')]
    buckets = [[] for _ in range(P)]
    for i, x in enumerate(input().split(' ')):
        grp = int(x)
        gid = grp % P
        buckets[gid].append(grp)

    num_fresh = 0
    num_fresh += len(buckets[0])
    # print(len(buckets[0]))

    # print(buckets)
    if P == 2:
        len_1 = len(buckets[1])
        if len_1 != 0:
            num_fresh += len_1 // 2 + 1 if len_1 % 2 != 0 else len_1 // 2
    elif P == 3:
        len_1 = len(buckets[1])
        len_2 = len(buckets[2])
        if len_1 != 0 or len_2 != 0:
            # print(len_1, len_2)
            min_len = min(len_1, len_2)
            max_len = max(len_1, len_2)
            num_fresh += min_len

            rem = max_len - min_len
            num_fresh += rem // 3 + 1 if rem % 3 != 0 else rem // 3
    elif P == 4:
        len_i = [len(buckets[i]) for i in range(1, 4)]
        min_b = 1
        max_b = 1
        min_len = len_i[0]
        max_len = len_i[0]
        for i in range(1, 3):
            if len_i[i] < min_len:
                min_len = len_i[i]
                min_b = i + 1
            if len_i[i] > max_len:
                max_len = len_i[i]
                max_b = i + 1
        # print(max_b, min_b)
    print(f'Case #{t}: {num_fresh}')

    # if t > 10:
        # break


    # exit()
