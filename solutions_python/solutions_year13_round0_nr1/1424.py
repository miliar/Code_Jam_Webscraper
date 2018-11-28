import sys

def check_rows(test_case):
    for row in test_case:
        sum_X = sum(1 if (m == 'X' or m == 'T') else 0 for m in row)
        sum_O = sum(1 if (m == 'O' or m == 'T') else 0 for m in row)
        if sum_X == 4:
            return 'X won'
        elif sum_O == 4:
            return 'O won'
    return None


def check_cols(test_case):
    # test case transposition
    test_case_t = map(list, zip(*test_case))
    return check_rows(test_case_t)


def check_diag(test_case):
    l = len(test_case[0])
    d1 = [test_case[i][i] for i in range(l)]
    d2 = [test_case[l-1-i][i] for i in range(l-1, -1, -1)]
    diags = [d1, d2]
    return check_rows(diags)


def check_test_case(test_case):
    # check rows
    check_r = check_rows(test_case)
    if check_r is not None:
        return check_r

    check_c = check_cols(test_case)
    if check_c is not None:
        return check_c

    check_d = check_diag(test_case)
    if check_d is not None:
        return check_d

    check_gameover = [1 for row in test_case if '.' in row]
    if not check_gameover:
        return "Draw"
    else:
        return "Game has not completed"


def solve(filename):
    with open(filename, 'r') as input_f:
        T = int(input_f.readline())
        for x in range(0, T):
            # start test case
            test_case = [list(input_f.readline().strip()) for r in range(0, 4)]

            r = check_test_case(test_case)

            print "Case #%s: %s" % (x+1, r)
            input_f.readline()

if __name__ == '__main__':
    filename = sys.argv[1]
    solve(filename)
