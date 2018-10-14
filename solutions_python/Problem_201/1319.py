from math import log2
from math import floor


def read_one(stream, type_to_read=int):
    return type_to_read(stream.readline().strip())


def read_several(stream, type_to_read=int):
    return [type_to_read(x) for x in stream.readline().strip().split()]


def next(N):
    if N % 2 == 0:
        return N//2, N//2 - 1
    else:
        return (N-1)//2, (N-1)//2


def find_best_position(stals):
    #print(stals)
    distances = [[-1, -1] for s in stals]
    so_far = 0
    for i in range(1, N+1):
        if not stals[i]:
            distances[i][0] = so_far
            so_far += 1
        else:
            so_far = 0

    so_far = 0
    for i in range(N, 0, -1):
        if not stals[i]:
            distances[i][1] = so_far
            so_far += 1
        else:
            so_far = 0

    #print(distances)
    min_distances = [min(a, b) for a, b in distances]
    max_distances = [max(a, b) for a, b in distances]
    #print("max: ", max_distances)
    #print("min: ", min_distances)
    maxs_of_min = []
    max_value = -1
    for i, m in enumerate(min_distances):
        if m > max_value:
            maxs_of_min = [i]
            max_value = m
        elif m == max_value:
            maxs_of_min.append(i)

    #print("maxs_of_min", maxs_of_min)
    assert maxs_of_min
    if len(maxs_of_min) == 1:
        pos = maxs_of_min[0]
        return min_distances[pos], max_distances[pos], pos

    maxs_of_max = 0
    max_value = -1
    for i in maxs_of_min:
        m = max_distances[i]
        if m > max_value:
            max_value = m
            maxs_of_max = [i]
        elif m == max_value:
            maxs_of_max.append(i)

    assert maxs_of_max
    #print("max of maxs", maxs_of_max)
    pos = maxs_of_max[0]
    return min_distances[pos], max_distances[pos], pos


def solve_small(N, K):
    stals = [False for _ in range(N+2)]
    stals[0] = True
    stals[-1] = True
    n_users = 0
    minLR, maxLR = 0, 0
    while n_users < K:
        minLR, maxLR, pos = find_best_position(stals)
        #print(minLR, maxLR, pos)
        stals[pos] = True
        n_users += 1
    return maxLR, minLR


def solve(N, K):
    # print("N, K", N, K)
    p = int(floor(log2(K)))  # 2^p < K <= 2^p+1

    n_users_done = int(2**p - 1)

    remaining_stals = N - n_users_done

    # remaining space are of size min_space or min_space + 1
    min_space = remaining_stals // (n_users_done + 1)
    n_big_spaces = remaining_stals % (n_users_done + 1)
    # n_small_spaces = (n_users_done + 1) - n_big_spaces
    n_users_remaining = K - n_users_done

    # print("p: ", p)
    # print("n_users_done: ", n_users_done)
    # print("remaining_stals: ", remaining_stals)
    # print("min_space: ", min_space)
    # print("n_big_spaces: ", n_big_spaces)
    # print("n_small_spaces: ", n_small_spaces)
    # print("n_users_remaining: ", n_users_remaining)
    if n_users_remaining <= n_big_spaces:
        return next(min_space + 1)
    else:
        return next(min_space)


if __name__ == "__main__":
    import sys
    stream = sys.stdin
    T = read_one(stream, int)
    for t in range(T):
        N, K = read_several(stream, int)
        solution = solve(N, K)
        print("Case #{id}: {maxLR} {minLR}".format(id=t+1, maxLR=solution[0], minLR=solution[1]))