import math


def is_all_happy(l):
    all(item[2] == 1 for item in l)


def flip(panc):
    if panc == '+':
        return '-'
    else:
        return '+'


def flip_row(row, ind, k_number):
    new_row = list(row)
    new_row[ind:ind + k_number] = [flip(ch) for ch in new_row[ind:ind + k_number]]
    return ''.join(new_row)


def find_min_flip(pancake_row, k_number):
    n_pancake = len(pancake_row)
    expected_value = ''.join(['+' for _ in range(n_pancake)])
    di = {pancake_row: 0}

    for _ in range(2 ** k_number + 1):
        for index in range(n_pancake - k_number + 1):
            to_insert = [(flip_row(state, index, k_number), step + 1) for state, step in di.items()]
            for new_s, new_step in to_insert:
                di[new_s] = min(di.get(new_s, 9999999999999), new_step)
        min_flip = di.get(expected_value, -1)
        if min_flip != -1:
            return min_flip

    return -1

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    pancake_line, k = [s for s in input().split()]
    min_f = find_min_flip(pancake_line, int(k))
    ans = 'IMPOSSIBLE'
    if min_f != -1:
        ans = min_f

    print("Case #{}: {}".format(i, ans))
