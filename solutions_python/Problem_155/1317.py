__author__ = 'jakub.bibro'


def solve(shy_levels):
    already_standing = 0
    to_invite = 0
    for shy_level, num_of_people in enumerate(shy_levels):
        if num_of_people > 0 and shy_level > already_standing:
            to_invite += shy_level - already_standing
            already_standing += to_invite
        already_standing += num_of_people

    return to_invite

if __name__ == '__main__':
    test_cases = int(raw_input())
    shy_levels_map = {}
    for i in range(0, test_cases):
        max_shy_level, shy_levels = raw_input().split(' ')
        max_shy_level = int(max_shy_level)
        shy_levels = [int(l) for l in shy_levels]
        shy_levels_map = dict((ind, l) for ind, l in enumerate(shy_levels))
        solution = solve(shy_levels)
        print('Case #{}: {}'.format(i + 1, solution))