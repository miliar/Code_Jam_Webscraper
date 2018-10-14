import sys

sys.setrecursionlimit(1000000)

WELCOME = 'welcome to code jam'

def memoize(func):
    results = {}
    def wrapper(*args):
        if args not in results:
            results[args] = func(*args)
        return results[args]
    return wrapper

def solve(line):
    @memoize
    def match(i, j):
        if i >= len(WELCOME):
            return 1
        elif j >= len(line):
            return 0
        if WELCOME[i] == line[j]:
            return (match(i + 1, j + 1) + match(i, j + 1)) % 10000
        else:
            return match(i, j + 1)
    return match(0, 0)

def main():
    N = int(raw_input())
    for case in xrange(N):
        print 'Case #%d: %04d' % (case + 1, solve(raw_input()))

if __name__ == '__main__':
    main()
