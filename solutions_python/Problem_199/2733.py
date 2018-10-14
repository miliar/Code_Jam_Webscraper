import sys

def line():
    return sys.stdin.readline().strip()

def ints(s):
    return [int(t) for t in s.split()]


def solve(sides, k):
    n = 0

    for i in range(len(sides) - k + 1):
        if sides[i] == '-':
            n += 1
            for j in range(k):
                if sides[i+j] == '-':
                    sides[i+j] = '+'
                else:
                    sides[i+j] = '-'

    for i in range(len(sides) - k + 1, len(sides)):
        if sides[i] == '-':
            return 'IMPOSSIBLE'
    return n

def main():
    tc = int(line())
    for i in range(1,tc+1):
        s = line()
        sides, k = s.split()
        sides = list(sides)
        k = int(k)
        print 'Case #%s: %s' % (i, solve(sides, k))

main()
