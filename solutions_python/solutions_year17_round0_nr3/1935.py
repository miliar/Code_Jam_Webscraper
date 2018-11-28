from itertools import groupby
import math

"""
    I KNOW ITS SLOW BUT I WANTED TO TRY THIS SOLUTION ANYWAY
"""
FREE = False
OCCUPIED = True


def get_stall_value(stalls, stall_index):
    left_free_space = right_free_space = 0
    tmp_index = stall_index

    while True:
        tmp_index -= 1
        if stalls[tmp_index] == OCCUPIED:
            break
        left_free_space += 1

    tmp_index = stall_index
    while True:
        tmp_index += 1
        if stalls[tmp_index] == OCCUPIED:
            break
        right_free_space += 1

    return left_free_space, right_free_space


def go_into_next_stall(stalls):
    final_index = 0

    grouped = groupby(stalls)
    max_len = 0
    for key, group in groupby(stalls):
        if key == FREE:
            max_len = max(max_len, len(list(group)))

    for key, group in grouped:
        group = list(group)
        group_len = len(group)
        if key == OCCUPIED or group_len != max_len:
            final_index += group_len
        else:
            final_index += int((group_len - 1) / 2)
            l_val, r_val = math.ceil((group_len - 1) / 2), math.floor((group_len - 1) / 2)
            break

    stalls[final_index] = OCCUPIED
    return l_val, r_val


def get_values(nbr_stalls, nbr_people):
    stalls = [FREE] * nbr_stalls
    stalls = [OCCUPIED] + stalls + [OCCUPIED]

    for people in range(nbr_people):
        l_val, r_val = go_into_next_stall(stalls)
    return l_val, r_val


def main():
    nbr_rows = int(input())

    for nbr_row in range(1, nbr_rows + 1):
        nbr_stalls, nbr_people = map(int, input().split())
        l_val, r_val = get_values(nbr_stalls, nbr_people)
        print("Case #{nbr_rows}: {l_val} {r_val}".format(
            nbr_rows=nbr_row, l_val=l_val, r_val=r_val))


if __name__ == "__main__":
    main()
