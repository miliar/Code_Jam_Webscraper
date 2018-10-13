import sys


# Cheat chart
# Made by little thinking and hand writing...
# if x = 1, GABRIEL always win.
# if x = 2, GABRIEL win if R x C is even.
# if x = 3, GABRIEL win if R x C is 3 x 2, 3 x 3 or 3 x 4.(R, C are switchable)
# if x = 4, GABRIEL win if R x C is 4 x 4 or 4 x 3.(R, C are switchable)


def solve_case(x, r, c, case_number):
    if x == 1:
        print "Case #%d: GABRIEL" % case_number
    elif x == 2:
        if (r * c) % 2 == 0:
            print "Case #%d: GABRIEL" % case_number
        else:
            print "Case #%d: RICHARD" % case_number
    elif x == 3:
        if {r, c} == {3, 2} or {r, c} == {3, 3} or {r, c} == {3, 4}:
            print "Case #%d: GABRIEL" % case_number
        else:
            print "Case #%d: RICHARD" % case_number
    elif x == 4:
        if {r, c} == {4, 4} or {r, c} == {4, 3}:
            print "Case #%d: GABRIEL" % case_number
        else:
            print "Case #%d: RICHARD" % case_number
    else:
        # Should never comes here.
        print "Case %d: CANNOT SOLVE!" % case_number


def main():
    r = sys.stdin

    if len(sys.argv) > 1:
        r = open(sys.argv[1], 'r')

    total_cases = r.readline()
    for case_number in range(1, int(total_cases) + 1):
        xrc = map(int, r.readline().strip().split(' '))
        solve_case(xrc[0], xrc[1], xrc[2], case_number)


if __name__ == '__main__':
    main()
