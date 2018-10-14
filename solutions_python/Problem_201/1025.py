import math

def get_max_min_L_R(N, K):
    depth = math.floor(math.log(K, 2))
    number_in_depth = math.pow(2, depth)
    index_in_depth = K - (number_in_depth - 1) - 1
    sum_in_depth = N - (number_in_depth - 1)
    large_number_in_depth = math.floor(N / number_in_depth)
    small_number_in_depth = large_number_in_depth - 1
    number_of_large_number_in_depth = sum_in_depth - number_in_depth * small_number_in_depth
    if index_in_depth < number_of_large_number_in_depth:
        stall_group_size = large_number_in_depth
    else:
        stall_group_size = small_number_in_depth
    if stall_group_size % 2 == 0:
        return (stall_group_size / 2, stall_group_size / 2 - 1)
    else:
        return ((stall_group_size-1) / 2, (stall_group_size-1) / 2)

T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split()]
    max_L_R, min_L_R = get_max_min_L_R(N, K)

    print("Case #%d: %d %d" % (t+1, max_L_R, min_L_R))