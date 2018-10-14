import sys

file_name = "A-large-practice"
sys.stdin = open(file_name + ".in", "r")
sys.stdout = open(file_name + ".out", "w")
input_line = sys.stdin.readline


def check_last_minus_index(pancakes):
    for i in range(len(pancakes)-1, -1, -1):
        if pancakes[i] == '-':
            return i


def check_all_happy(pancakes, flipper_size):
    is_happy = 1
    for i in range(len(pancakes)-1, -1, -1):
        if pancakes[i] == '-':
            is_happy = 0
            break
    if 0 <= i < flipper_size-1 and is_happy == 0:
        is_happy = "IMPOSSIBLE"
    return is_happy


def flip_pancakes(pancakes, index, flipper_size):
    pancakes_to_list = list(pancakes)
    for i in range(index, index-flipper_size, -1):
        if pancakes_to_list[i] == '-':
            pancakes_to_list[i] = '+'
        else:
            pancakes_to_list[i] = '-'
    return ''.join(pancakes_to_list)


for case in range(1, int(input_line())+1):
    line_in_to_list = input_line().split()
    S = line_in_to_list[0]
    K = int(line_in_to_list[1])

    count = 0

    while 1:
        if check_all_happy(S, K) == 1:
            result = count
            break
        elif check_all_happy(S, K) == "IMPOSSIBLE":
            result = "IMPOSSIBLE"
            break
        else:
            count += 1
            i = check_last_minus_index(S)
            S = flip_pancakes(S, i, K)

    print("Case #{0}: {1}".format(case, result))



