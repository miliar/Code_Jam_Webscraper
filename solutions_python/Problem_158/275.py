import sys


def get_winner(x, r, c):
    if x == 1:
        return 'GABRIEL'
    m = r * c

    if x == 2:
        if m % 2 == 0:
            return 'GABRIEL'
        else:
            return 'RICHARD'

    if x == 3:
        if m % 3 == 0:
            if r == 1:
                return 'RICHARD'
            else:
                return 'GABRIEL'
        else:
            return 'RICHARD'

    if x == 4:
        if m % 4 == 0:
            if r == 1 or r == 2:
                return 'RICHARD'
            else:
                return 'GABRIEL'
        else:
            return 'RICHARD'
    return None


def main():
    t = int(sys.stdin.readline())
    for k in range(t):
        x, r, c = map(int, sys.stdin.readline().strip().split())
        r, c = min(r, c), max(r, c)

        winner = get_winner(x, r, c)
        print ('Case #%d: %s' % (k + 1, winner))

if __name__ == '__main__':
    main()
