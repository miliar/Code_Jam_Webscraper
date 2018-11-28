import sys


def solve(line):
    smax, ss = line.strip().split(' ')
    standing = 0
    invited = 0
    for s, n in enumerate(int(x) for x in ss):
        invited += max(s-standing, 0)
        standing += max(s-standing, 0) + n
    return invited

if __name__ == '__main__':
    sys.stdin.readline()
    for t, l in enumerate(sys.stdin):
        print("Case #{}: {}".format(t+1, solve(l)))


