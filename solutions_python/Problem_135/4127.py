import sys


def test():
    x = int(sys.stdin.readline().strip())
    rows = [sys.stdin.readline().strip().split() for _ in range(4)]
    row1 = rows[x-1]

    y = int(sys.stdin.readline().strip())
    rows = [sys.stdin.readline().strip().split() for _ in range(4)]
    row2 = rows[y-1]

    z = set(row1) & set(row2)

    if len(z) == 0:
        return 'Volunteer cheated!'
    elif len(z) == 1:
        return z.pop()
    elif len(z):
        return 'Bad magician!'


def main():
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        print 'Case #%d: %s' % (i + 1, test())

main()
