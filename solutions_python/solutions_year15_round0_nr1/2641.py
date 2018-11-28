#! /usr/bin/env python2.7
def solve(shyness_levels):
    needed = 0
    cur_standing = shyness_levels[0]

    for shyness, num_people in enumerate(shyness_levels[1:], 1):
        if num_people:
            needed_for_shyness = shyness - cur_standing
            if needed_for_shyness > 0:
                needed += needed_for_shyness
                cur_standing += needed_for_shyness
            cur_standing += num_people

    return needed


if __name__ == '__main__':
    for i in range(1, int(raw_input())+1):
        _, shyness_levels = raw_input().split()


        print "Case #{0}: {1}".format(i, solve(map(int, list(shyness_levels))))
