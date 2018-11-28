import sys

def find_closest(idx, idx_list):
    if len(idx_list) == 0:
        return None
    for i in xrange(len(idx_list)):
        if idx_list[i] >= idx and (i == 0 or idx_list[i - 1] < idx):
            return idx_list[i]
        if idx_list[i] <= idx and (i == len(idx_list) - 1 or idx_list[i + 1] > idx):
            return idx_list[i]
    return None # Should never happen


def spread_sides(cake):
    for row in cake:
        non_empty = [i for i, char in enumerate(row) if char != '?']
        for i in xrange(len(row)):
            idx = find_closest(i, non_empty)
            if idx is not None:
                row[i] = row[idx]


def find_block(cake, start_i, start_j):
    letter = cake[start_i][start_j]

    if letter == '?':
        return letter, start_i, start_j, start_i, start_j

    horizontal_end = len(cake[start_i]) - 1 - cake[start_i][::-1].index(letter)
    vertical_end = start_i
    while vertical_end + 1 < len(cake) and cake[vertical_end + 1][start_j] == '?' and cake[vertical_end + 1][horizontal_end] == '?':
        vertical_end += 1
    vertical_start = start_i
    while vertical_start - 1 >= 0 and cake[vertical_start - 1][start_j] == '?' and cake[vertical_start - 1][horizontal_end] == '?':
        vertical_start -= 1

    return letter, vertical_start, start_j, vertical_end, horizontal_end


def fill_block(cake, letter, start_i, start_j, end_i, end_j):
    for i in range(start_i, end_i + 1):
        for j in range(start_j, end_j + 1):
            cake[i][j] = letter

def spread_down(cake):
    for i in range(len(cake)):
        for j in range(len(cake[i])):
            letter, start_i, start_j, end_i, end_j = find_block(cake, i, j)
            fill_block(cake, letter, start_i, start_j, end_i, end_j)


def display(cake):
    for R in cake:
        for C in R:
            sys.stdout.write(C)
            sys.stdout.flush()
        print("")


t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
    R, C = [int(s) for s in raw_input().split(" ")]
    cake = []
    for k in xrange(R):
        cake.append(list(raw_input()))
    print("Case #{}:".format(i))
    spread_sides(cake)
    spread_down(cake)
    display(cake)
