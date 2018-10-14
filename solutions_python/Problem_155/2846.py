import sys


def solve(levels):
    standing = 0
    needed = 0
    for level, people in enumerate(levels):
        if level > standing:
            n = level - standing
            needed += n
            standing += n
        standing += people
    return needed


def read_numbers(line=None):
    if line is None:
        line = sys.stdin.readline()
    numbers = line.strip().split()
    return [int(n) for n in numbers]


if __name__ == '__main__':
    T = int(raw_input())
    for t in range(T):
        line = sys.stdin.readline()
        _, levels = line.strip().split()
        levels = [int(c) for c in levels]
        print "Case #%d: %d" % (t + 1, solve(levels))
