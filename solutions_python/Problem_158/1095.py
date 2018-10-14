import sys


def handle_case():
    nums = sys.stdin.readline().strip().split()
    X, R, C = map(lambda x: int(x), nums)

    # if can't fit a piece
    if R*C < X:
        return 'RICHARD'

    # if can't evenly fill space
    if (R*C) % X:
        #print 'here: {}'.format((R*C) % X)
        return 'RICHARD'

    # if too skinny
    if X > 2 \
            and (R == 1 or C == 1) \
            and (X > R or X > C):
        return 'RICHARD'

    if X > 3 \
            and (R == 2 or C == 2):
        return 'RICHARD'

    return 'GABRIEL'


if __name__ == '__main__':
    cases = int(sys.stdin.readline().strip())

    for i in xrange(1, cases+1):
        answer = handle_case()
        print "Case #{}: {}".format(i, answer)
