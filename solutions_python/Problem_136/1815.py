import sys


def read_input():
    return [float(x) for x in sys.stdin.readline().strip().split()]

def solve():
    c, f, x = read_input()
    s = 2

    accumulator = 0
    t = x / s
    while True:
        accumulator += c / s
        s += f
        t1 = accumulator + x / s
        if t1 > t:
            break
        t = t1

    return t


def main():
    T = int(sys.stdin.readline().strip())
    for case in xrange(T):
        print 'Case #{0}: {1:.7f}'.format(case + 1, solve())


if __name__ == '__main__':
    main()
