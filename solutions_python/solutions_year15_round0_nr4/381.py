__author__ = 'ctynan'


def main():
    f_in = open('/Users/ctynan/Downloads/D-small-attempt2.in', 'r')
    f_out = open('/Users/ctynan/Downloads/D-small-attempt2.out', 'w')

    T = int(f_in.readline())

    for tst in range(T):
        X, R, C = f_in.readline().strip('\n').split(' ')
        X, R, C = int(X), int(R), int(C)

        r = max(R, C)
        c = min(R, C)

        winner = ''

        if X == 1:
            winner = 'GABRIEL'
        if X == 2:
            if (r * c) % 2 == 1:
                winner = 'RICHARD'
            else:
                winner = 'GABRIEL'
        if X == 3:
            if r < 3 or (r == 3 and c == 1) or (r == 4 and c in (1, 2, 4)):
                winner = 'RICHARD'
            else:
                winner = 'GABRIEL'
        if X == 4:
            if r == 4 and c >= 3:
                winner = 'GABRIEL'
            else:
                winner = 'RICHARD'

        f_out.write(("Case #%i: %s\n") % (tst + 1, winner))

    return

main()

