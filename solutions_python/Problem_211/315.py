from decimal import Decimal, getcontext
getcontext().prec = 6
import copy

t = int(input())
for i in range(1, t + 1):
    [N, K]= [int(s) for s in input().split(" ")]
    U = float(input())
    orig_P = [float(p) for p in input().split(" ")]
    P = copy.deepcopy(orig_P)

    rest_U = U

    # print(N, K, U)
    # print(orig_P)

    while rest_U != 0.0:
        min_p = 1.0
        for p in P:
            if p < min_p:
                min_p = p

        min_p_set = []
        index = 0
        for p in P:
            if p == min_p:
                min_p_set.append(index)
            index += 1

        # print('min_p_set: ' + str(min_p_set))

        min_second_p = 1.0
        for p in P:
            if p != min_p and p < min_second_p:
                min_second_p = p

        if rest_U > float(Decimal(len(min_p_set)) * Decimal((min_second_p - min_p))):
            for set_index in min_p_set:
                P[set_index] = min_second_p
            rest_U -= float(Decimal(len(min_p_set)) * Decimal((min_second_p - min_p)))
        else:
            part_U = float(Decimal(rest_U) / Decimal(len(min_p_set)))
            for set_index in min_p_set:
                P[set_index] += part_U
            rest_U = 0.0

        # print('rest_U: ' + str(rest_U))
        # print('P: ' + str(P))

    total_P = 1
    for p in P:
        total_P *= p


    print("Case #{}: {}".format(i, total_P, orig_P, P))
