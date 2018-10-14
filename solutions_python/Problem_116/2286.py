#! /usr/bin/env python

import sys


def parse_line(s):
    return [s[i] for i in range(len(s))]


def from_lines(lines):
    """
    Read the next 4 lines of input and turn them into an array
    """
    return [parse_line(line) for line in lines]


def check_status(row):
    """
    Check the status of the game given a row
    """

    n_o = row.count('O')
    n_t = row.count('T')
    n_x = row.count('X')

    # O won
    if (n_o + n_t) == 4:
        return 'O'

    # X won
    if (n_x + n_t) == 4:
        return 'X'

    return 0


def check_rows(grid):
    """
    Check the rows
    """

    for i in range(4):

        status = check_status(grid[i])
        if status != 0:
            return status

    return 0


def check_columns(grid):
    """
    Check the colums
    This is equivalent to checking the rows of the transposed of the grid
    """
    return check_rows(zip(*grid))


def check_diagonals(grid):
    """
    Check diagonals
    """

    d1 = [grid[0][0], grid[1][1], grid[2][2], grid[3][3]]
    status = check_status(d1)
    if status != 0:
        return status

    d2 = [grid[0][3], grid[1][2], grid[2][1], grid[3][0]]
    status = check_status(d2)
    if status != 0:
        return status

    return 0


def check_grid(grid):
    """
    """

    status = check_rows(grid)
    if status != 0:
        return status

    status = check_columns(grid)
    if status != 0:
        return status

    status = check_diagonals(grid)
    if status != 0:
        return status

    return 0


def main():
    """
    """
    
    f_in  = open(sys.argv[1], 'r')
    f_out = open(sys.argv[2], 'w')

    T = int(f_in.readline())

    for case_number in range(T):
        
        lines = [f_in.readline() for i in range(4)]
        f_in.readline()

        grid = from_lines(lines)
        status = check_grid(grid)
        
        f_out.write("Case #{}: ".format(case_number+1))

        if status == 0:

            if sum(map(lambda x: x.count('.'), grid)):
                f_out.write("Game has not completed\n")
            else:
                f_out.write("Draw\n")

        elif status == 'O':
            f_out.write("O won\n")

        elif status == 'X':
            f_out.write("X won\n")

    f_in.close()
    f_out.close()


if __name__ == "__main__":
    main()
