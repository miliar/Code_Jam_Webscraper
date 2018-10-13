import math

def output(t, res):
    casestr = "Case #" + str(t+1) + ": "
    status = str(res) if res is not None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine


def main():
    T = int(raw_input())

    for t in xrange(T):
        N, M = map(int, raw_input().split(' '))
        grid = [['.']*N for x in xrange(N)]
        for m in xrange(M):
            model, R, C = raw_input().split(' ')
            R = int(R)-1
            C = int(C)-1
            grid[R][C] = model

        #print grid
        modified = {}
        for i in xrange(N/2 + 1):
            for j in xrange(N):
                add_if_possible(grid, modified, '+', i, j)
                add_if_possible(grid, modified, '+', N - 1 - i, j)

        for i in xrange(N):
            for j in xrange(N):
                add_if_possible(grid, modified, 'x', i, j)

        for i in xrange(N):
            for j in xrange(N):
                add_if_possible(grid, modified, 'o', i, j)

        y = get_y(grid)
        output(t, str(y) + ' ' + str(len(modified)))
        for m in modified:
            print modified[m], m

        # for g in grid:
        #     print g

        # if not valid(grid):
        #     print "Something went very wrong.", " Last grid:"
        #     print grid
        #     exit()

        #print grid
        #print "----"


def get_y(grid):
    y = 0
    N = len(grid)
    for i in xrange(N):
        for j in xrange(N):
            m = grid[i][j]
            if m == 'o':
                y += 2
            elif m == '+' or m == 'x':
                y += 1

    return y


def add_if_possible(grid, modified, model, R, C):
    prev = grid[R][C]
    if prev == model:
        return 0

    if prev != '.' and model != 'o':
        return 0

    # if not valid(grid):
    #     print "Something went very wrong.", model , R, C, " Last grid:"
    #     print grid
    #     exit()

    grid[R][C] = model
    if not valid_quick(grid, R, C):
        grid[R][C] = prev
        return 0

    add_to_modified(modified, model, R, C)
    return 1

def add_to_modified(modified, model, R, C):
    cell = str(R+1) + " " + str(C+1)
    modified[cell] = model

def valid_quick(grid, R, C):
    if not valid_row(grid, R):
        return False

    if not valid_col(grid, C):
        return False

    # ->
    if not valid_diag1(grid, R, C):
        return False

    # <-
    if not valid_diag2(grid, R, C):
        return False

    return True


def valid_row(grid, R):
    if len(filter(lambda x: x != '+' and x != '.', grid[R])) >= 2:
        return False
    return True


def valid_col(grid, C):
    N = len(grid)
    if len(filter(lambda j: grid[j][C] != '+' and grid[j][C] != '.', xrange(N))) >= 2:
        return False
    return True


def valid_diag1(grid, R, C):
    N = len(grid)
    if R >= C:
        i = R - C
        if len(filter(lambda j: grid[i + j][j] != 'x' and grid[i + j][j] != '.', xrange(N - i))) >= 2:
            return False
    else:
        i = C - R
        if len(filter(lambda j: grid[j][i + j] != 'x' and grid[j][i + j] != '.', xrange(N - i))) >= 2:
            return False
    return True


def valid_diag2(grid, R, C):
    N = len(grid)
    if R + C <= N-1:
        i = N - 1 - R - C
        if len(filter(lambda j: grid[N - 1 - i - j][j] != 'x' and grid[N - 1 - i - j][j] != '.', xrange(N - i))) >= 2:
            return False
    else:
        i = R + C - N + 1
        if len(filter(lambda j: grid[N - 1 - j][i + j] != 'x' and grid[N - 1 - j][i + j] != '.', xrange(N - i))) >= 2:
            return False
    return True


def valid(grid):
    N = len(grid)
    for i in xrange(N):
        if not valid_row(grid, i):
            return False

        if not valid_col(grid, i):
            return False

        # ->
        if not valid_diag1(grid, i, 0):
            return False

        if not valid_diag1(grid, 0, i):
            return False

        # <-
        if not valid_diag2(grid, i, 0):
            return False

        if not valid_diag2(grid, N-1, i):
            return False

    return True

if __name__ == "__main__":
    main()