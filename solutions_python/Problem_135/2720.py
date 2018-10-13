def read_matrix():
    l = []
    for x in range(4):
        line = raw_input()
        l.append([int(x) for x in line.split()])
    return l


def handle_case(case_num):
    row_num1 = int(raw_input())
    mat1 = read_matrix()
    row_num2 = int(raw_input())
    mat2 = read_matrix()
    solve_case(case_num, row_num1, mat1, row_num2, mat2)


def validate_rownum(row_num):
    if row_num < 1 or row_num > 4:
        return False
    return True


BAD_MAGICIAN, CHEAT = -1, 17


def print_case(case_num, out):
    if out == BAD_MAGICIAN:
        out = "Bad magician!"
    elif out == CHEAT:
        out = "Volunteer cheated!"
    print "Case #%d: %s" % (case_num, out)


def solve_case(case_num, row_num1, mat1, row_num2, mat2):
    if not validate_rownum(row_num1) or not validate_rownum(row_num2):
        return print_case(case_num, CHEAT)
    set1 = set(mat1[row_num1 - 1])
    set2 = set(mat2[row_num2 - 1])
    intersection = set1 & set2
    l = len(intersection)
    if l == 0:
        return print_case(case_num, CHEAT)
    elif l == 1:
        return print_case(case_num, intersection.pop())
    else:
        return print_case(case_num, BAD_MAGICIAN)


def main():
    n_cases = int(raw_input())
    for case in range(1, n_cases + 1):
        handle_case(case)


if __name__ == '__main__':
    main()
