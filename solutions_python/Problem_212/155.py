import math

def solve(N, P, G):
    if P == 2:
        num_0 = len([g for g in G if g % 2 == 0])
        num_1 = len([g for g in G if g % 2 == 1])

        return num_0 + math.ceil(num_1 / 2)
    elif P == 3:
        num_0 = len([g for g in G if g % 3 == 0])
        num_1 = len([g for g in G if g % 3 == 1])
        num_2 = len([g for g in G if g % 3 == 2])
        num_coupled_g = min(num_1, num_2)

        return num_0 + num_coupled_g + math.ceil((num_1 - num_coupled_g) / 3) + math.ceil((num_2 - num_coupled_g) / 3)
    else:
        num_0 = len([g for g in G if g % 4 == 0])
        num_1 = len([g for g in G if g % 4 == 1])
        num_2 = len([g for g in G if g % 4 == 2])
        num_3 = len([g for g in G if g % 4 == 3])

        max_num_group = num_0

        num_coupled_g_2_2 = num_2 // 2
        max_num_group += num_coupled_g_2_2
        num_coupled_g_1_3 = min(num_1, num_3)
        max_num_group += num_coupled_g_1_3

        num_2 -= 2 * num_coupled_g_2_2
        num_1 -= num_coupled_g_1_3
        num_3 -= num_coupled_g_1_3

        num_coupled_g_1_1_2 = min(num_1 // 2, num_2)
        max_num_group += num_coupled_g_1_1_2

        num_2 -= num_coupled_g_1_1_2
        num_1 -= 2 * num_coupled_g_1_1_2

        num_coupled_g_3_3_2 = min(num_3 // 2, num_2)
        max_num_group += num_coupled_g_3_3_2

        num_2 -= num_coupled_g_3_3_2
        num_3 -= 2 * num_coupled_g_3_3_2

        num_coupled_g_1_1_1_1 = num_1 // 4
        max_num_group += num_coupled_g_1_1_1_1
        num_1 -= 4 * num_coupled_g_1_1_1_1

        num_coupled_g_3_3_3_3 = num_3 // 4
        max_num_group += num_coupled_g_3_3_3_3
        num_3 -= 4 * num_coupled_g_3_3_3_3

        if num_1 + num_2 + num_3 > 0:
            max_num_group += 1

        return max_num_group

T = int(input())
for t in range(T):
    N, P = [int(x) for x in input().split()]
    G = [int(x) for x in input().split()]

    max_num_group = solve(N, P, G)

    print("Case #%d: %d" % (t+1, max_num_group))