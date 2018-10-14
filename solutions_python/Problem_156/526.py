import sys
import math


def half_floor_as_int(x):
    return int(math.floor(float(x) / 2))


def half_ceil_as_int(x):
    return int(math.ceil(float(x) / 2))


def pancake_calc(pancakes, count):
    m = max(pancakes)
    if m < 1:
        return count

    count += 1

    candidates = [pancake_calc(map(lambda x: x - 1, pancakes), count)]

    if m > 1:
        new_pancakes = pancakes[:]
        new_pancakes.remove(m)
        new_pancakes.append(half_ceil_as_int(m))
        new_pancakes.append(half_floor_as_int(m))
        candidates.append(pancake_calc(new_pancakes, count))

    # 9 can be split into three 3s. This is sometime faster, even though this operation takes 2 minutes.
    # I haven't be able to generalize this yet...
    if m == 9:
        new_pancakes = pancakes[:]
        new_pancakes.remove(m)
        new_pancakes.append(6)
        new_pancakes.append(3)
        candidates.append(pancake_calc(new_pancakes, count))

    return min(candidates)


def solve_case(pancakes, case_number):
    print "Case #%d: %d" % (case_number, pancake_calc(pancakes, 0))


def main():
    r = sys.stdin

    if len(sys.argv) > 1:
        r = open(sys.argv[1], 'r')

    total_cases = r.readline()
    for case_number in range(1, int(total_cases) + 1):
        r.readline()  # skip
        solve_case(map(int, r.readline().strip().split(' ')), case_number)


if __name__ == '__main__':
    main()
