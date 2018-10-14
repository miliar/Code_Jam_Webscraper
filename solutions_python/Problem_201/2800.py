def max_min_l_r_s(num):
    return int(num / 2), int(num / 2 - (num+1) % 2)


def find_last_max_min(n_stall, k_person):
    di = {n_stall: 1}
    last_max_min = 0, 0
    for _ in range(k_person):
        max_empty_row = max(di.keys())
        num_max_empty_row = di.pop(max_empty_row)
        if num_max_empty_row > 1:
            di[max_empty_row] = num_max_empty_row - 1
        last_max_min = max_min_l_r_s(max_empty_row)
        max_lr, min_lr = last_max_min
        di[max_lr] = di.get(max_lr, 0) + 1
        di[min_lr] = di.get(min_lr, 0) + 1

    return last_max_min


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split()]

    max_lrs, min_lrs = find_last_max_min(n, k)

    print("Case #{}: {} {}".format(i, max_lrs, min_lrs))
