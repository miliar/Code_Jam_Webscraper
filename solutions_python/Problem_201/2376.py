MAX = 999999999


def get_stalls_stats(stalls):
    stall_stats = []  # [-1, (0,3), (1,2), (2,1), (3,0), -1]
    for index, item in enumerate(stalls):
        if item:
            stall_stats.append(None)
            continue

        left_space = 0
        for i in range(index - 1, -1, -1):
            if stalls[i]:
                break
            left_space += 1

        right_space = 0
        for i in range(index + 1, len(stalls)):
            if stalls[i]:
                break
            right_space += 1

        stall_stats.append((left_space, right_space))
    return stall_stats


def get_stall_stats(n, k):
    stalls = [1] + [0 for _ in range(n)] + [1]
    last_persons_index = 0
    for _ in range(k):
        stats = get_stalls_stats(stalls)

        # get max of mins
        max_value = 0
        for index, value in enumerate(stats):
            if not value:
                continue

            cur_min = min(value)
            if cur_min > max_value:
                max_value = cur_min

        indices = [index for index, value in enumerate(stats) if value and min(value) == max_value]

        if len(indices) == 1:
            last_persons_index = indices[0]
            stalls[indices[0]] = 1
            continue

        candidates = [(stats[index], index) for index in indices]
        max_value = max(candidates[0][0])
        max_index = candidates[0][1]
        for value, index in candidates:
            cur_max = max(value)
            if cur_max > max_value:
                max_value = cur_max
                max_index = index
        last_persons_index = max_index
        stalls[last_persons_index] = 1

    # stats = get_stalls_stats(stalls)
    return max(stats[last_persons_index]), min(stats[last_persons_index])


for index in range(1, int(input()) + 1):
    n, k = [int(item) for item in input().split()]
    left, right = get_stall_stats(n, k)
    print("Case #%s: %s %s" % (index, left, right))
