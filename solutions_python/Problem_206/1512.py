import sys


def read_int():
    return int(sys.stdin.readline().strip())


def read_ints():
    return map(int, sys.stdin.readline().strip().split())


def cruise_speed(positions, speeds, end_dist):
    times = [(end_dist - float(positions[i])) / speeds[i] for i in xrange(len(positions))]
    max_time = max(times)
    return end_dist / max_time


def solve_from_input():
    case_count = read_int()
    for c in xrange(1, case_count+1):
        end_dist, horse_count = read_ints()
        positions = []
        speeds = []
        for _ in xrange(horse_count):
            p, s = read_ints()
            positions.append(p)
            speeds.append(s)
        result = cruise_speed(positions, speeds, end_dist)
        sys.stdout.write('Case #{}: {:.6f}\n'.format(c, result))


if __name__ == '__main__':
    solve_from_input()
