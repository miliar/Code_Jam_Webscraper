from contextlib import closing
import sys


def open_argv():
    return open(sys.argv[1])


def recycle(i):
    s = str(i)
    return (int(s[i:]+s[:i]) for i in range(1, len(s)))


def how_many(a, b):
    numbers = set()
    for n in range(a, b + 1):
        for m in recycle(n):
            if n < m <= b:
                numbers.add((n, m))
    return len(numbers)


def main():
    with closing(open_argv()) as f:
        n = int(f.readline())

        for index in range(n):
            a, b = map(int, f.readline().split())

            result = how_many(a, b)

            print 'Case #{0}: {1}'.format(index + 1, result)


if __name__ == '__main__':
    main()
