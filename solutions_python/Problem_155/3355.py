with open('input', 'r') as file:
    input = file.read()

input = input.split('\n')
cases = int(input[0])


def solve(smax, levels):
    assert smax + 1 == len(levels)

    cur_standing = 0
    solved_level = 0
    to_add = 0

    while solved_level < smax + 1:
        # print("solved_level: {} cur_standing: {} to_add: {}".format(solved_level, cur_standing, to_add))
        if cur_standing + to_add >= solved_level:
            cur_standing += levels[solved_level]
            solved_level += 1
        else:
            to_add += solved_level - (to_add + cur_standing)

    return to_add

i = 1
for case in input[1:cases + 1]:
    case = case.split()
    smax = int(case[0])
    levels = [int(c) for c in case[1]]
    # print("case {} - smax: {} - levels: {}".format(i, smax, levels))
    print("Case #{}: {}".format(i, solve(smax, levels)))
    # print(x)

    i += 1
