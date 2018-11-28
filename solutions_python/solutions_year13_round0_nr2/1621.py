def main():
    with open('input.in', 'r') as f:
        tests = int(f.readline().strip())

        for x in xrange(tests):
            n, m = [int(i) for i in f.readline().strip().split(" ")]
            mat = []

            for i in xrange(n):
                mat.append([int(i) for i in f.readline().strip().split(" ")])

            print("Case #%d: %s" % (x+1, solve(n, m, mat)))


def solve(n, m, mat):
    # Mark all lines and cols as not deleted
    line_del = [False for i in xrange(n)]
    col_del = [False for i in xrange(m)]

    # Take all the elements from the matrix and sort them by value
    elems = []
    for i in xrange(n):
        for j in xrange(m):
            elems.append((mat[i][j], i, j))
    elems.sort()

    for (num, i, j) in elems:
        if not line_del[i] and not col_del[j]:
            if can_del_line(n, m, mat, i, mat[i][j]):
                line_del[i] = True
                for x in xrange(m):
                    mat[i][x] = 0
            elif can_del_col(n, m, mat, j, mat[i][j]):
                col_del[j] = True
                for x in xrange(n):
                    mat[x][j] = 0
            else:
                return "NO"

    return "YES"


def can_del_line(n, m, mat, i, val):
    for j in xrange(m):
        if mat[i][j] > val:
            return False

    return True


def can_del_col(n, m, mat, j, val):
    for i in xrange(n):
        if mat[i][j] > val:
            return False

    return True


if __name__ == '__main__':
    main()
