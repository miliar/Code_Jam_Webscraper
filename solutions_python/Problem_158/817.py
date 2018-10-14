def out(case, winner):
    out_str = 'Case #%d: %s\n' % (case + 1, winner)
    return out_str


def judge(x, r, c):
    if x == 1:
        return False

    elif x == 2:
        if r == c == 1:
            return True
        elif r == 1 and c == 3:
            return True
        elif r == 3 and c == 1:
            return True
        elif r == 3 and c == 3:
            return True
        return False

    elif x == 3:
        if r == 3 and c == 2:
            return False
        elif r == 2 and c == 3:
            return False
        elif r == 3 and c == 4:
            return False
        elif r == 3 and c == 3:
            return False
        elif r == 4 and c == 3:
            return False
        return True

    elif x == 4:
        if r == 3 and c == 4:
            return False
        elif r == 4 and c == 3:
            return False
        elif r == 4 and c == 4:
            return False
        return True


if __name__ == '__main__':
    f_in = open('D-small-attempt4.in', 'r')
    f_out = open('D-small-attempt4.out', 'w')

    test_num = f_in.readline()
    lines = f_in.readlines()

    for index, line in enumerate(lines):
        X, R, C = [int(n) for n in line.split(' ')]
        if judge(X, R, C):
            f_out.write(out(index, 'RICHARD'))
        else:
            f_out.write(out(index, 'GABRIEL'))
