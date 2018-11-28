def minmax(n, k):
    if k >= n:
        return "0 0"

    stalls = [1] + [0] * n + [1]

    for x in range(k):
        # fcn - farthest closest neighbour
        fcn = 0
        candidate_stalls = []
        store = {}
        table = {}

        for index in range(len(stalls)):
            stall = stalls[index]
            occupied = stall == 1

            if occupied:
                last_Ls = -1
                continue

            Ls = last_Ls + 1
            store[index] = Ls

            last_Ls = Ls

        for index in reversed(range(len(stalls))):
            stall = stalls[index]
            occupied = stall == 1

            if occupied:
                last_Rs = -1
                continue

            Ls = store[index]
            Rs = last_Rs + 1
            last_Rs = Rs

            cn = min(Ls, Rs)
            fn = max(Ls, Rs)
            table[index] = [fn , cn]
            if cn > fcn:
                fcn = cn
                candidate_stalls = [(index, fn)]
            elif cn == fcn:
                candidate_stalls.append((index, fn))

            ffn = 0
            chosen_indicies = []
            for stall_index, stall_fn in candidate_stalls:
                if stall_fn > ffn:
                    ffn = stall_fn
                    chosen_indicies = [stall_index]
                elif stall_fn == ffn:
                    chosen_indicies.append(stall_index)

        chosen_indicies.sort()
        chosen_stall = chosen_indicies[0]
        stalls[chosen_stall] = 1

    y, x = table[chosen_stall]
    return "{} {}".format(y, x)

    #     for index, occupied in enumerate(stal'ls'):
    #         if occupied == 1:
    #             LAST_Ls = -1
    #             LAST_Rs = None
    #             continue

    #         # find Ls
    #         if LAST_Ls is not None:
    #             Ls = LAST_Ls + 1

    #         # find Rs
    #         if LAST_Rs is not None:
    #             Rs = LAST_Rs - 1
    #         else:
    #             Rs = 0
    #             for z in range(index + 1, len(stalls)):
    #                 if stalls[z] == 0:
    #                     Rs += 1
    #                 else:
    #                     break

    #         # cn - closest neighbour
    #         LAST_Ls = Ls
    #         LAST_Rs = Rs
    #         cn = min(Ls, Rs)
    #         fn = max(Ls, Rs)
    #         table[index] = [fn , cn]
    #         if cn > fcn:
    #             fcn = cn
    #             candidate_stalls = [(index, fn)]
    #         elif cn == fcn:
    #             candidate_stalls.append((index, fn))

    #         ffn = 0
    #         chosen_indicies = []
    #         for stall_index, stall_fn in candidate_stalls:
    #             if stall_fn > ffn:
    #                 ffn = stall_fn
    #                 chosen_indicies = [stall_index]
    #             elif stall_fn == ffn:
    #                 chosen_indicies.append(stall_index)

    #     chosen_indicies.sort()
    #     chosen_stall = chosen_indicies[0]
    #     stalls[chosen_stall] = 1
    # y, x = table[chosen_stall]
    # return "{} {}".format(y, x)

cases = int(input())
for case in range(1, cases + 1):
    N, K = [int(x) for x in input().split(' ')]
    print("Case #{}: {}".format(case, minmax(N, K)))
