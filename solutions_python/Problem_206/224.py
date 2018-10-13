T = int(input())

for test_case_no in range(T):
    test_case_no = test_case_no + 1

    D, N_horses = [int(x) for x in input().split()]

    K, S = [], []
    for _ in range(N_horses):
        k, s = [int(x) for x in input().split()]
        K.append(k)
        S.append(s)

    max_tid = 0
    for (k, s) in zip(K, S):
        time_this_horse = (D - k) / s
        max_tid = max(time_this_horse, max_tid)

    our_max_speed = D / max_tid
    print("Case #{}: {}".format(test_case_no, our_max_speed))

