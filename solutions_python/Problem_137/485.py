import sys
import os.path

def main(lines):
    it = iter(lines)

    n_cases = int(next(it))

    case = 0

    for line in it:
        case += 1
        args = [int(x) for x in line.split()]
        print "Case #%d:" % case
        sol = solve(*args)
        print sol,
        if sol == "Impossible\n":
            # print args
            pass

    if case != n_cases:
        raise Exception("Wrong # of cases")


def solve(rows, cols, mines):
    if mines >= rows * cols:
        return "Impossible\n"
    if mines == rows * cols - 1:
        field = prepare_field(rows, cols)
        rows = len(field)
        cols = len(field[0])
        for i in range(rows):
            for j in range(cols):
                field[i][j] = "*"

        field[0][0] = "c"

        return str_field(field)

    if rows == 1:
        return "c" + (cols - mines - 1) * "." + mines * "*" + "\n"
    elif cols == 1:
        return "c\n" + (rows - mines - 1) * ".\n" + mines * "*\n"
    elif rows == 2:
        if mines > (cols - 2) * rows or mines % 2 != 0:
            return "Impossible\n"
        else:
            row_mines = mines/2
            buf = "c." + (cols - 2 - row_mines) * "." + row_mines * "*" + "\n"
            buf += ".." + (cols - 2 - row_mines) * "." + row_mines * "*" + "\n"
            return buf
    elif cols == 2:
        if mines > (rows - 2) * cols or mines % 2 != 0:
            return "Impossible\n"
        else:
            col_mines = mines/2
            buf = "c.\n..\n"
            buf += (rows - 2 - col_mines) * "..\n"
            buf += col_mines * "**\n"

            return buf

    else:
        field = prepare_field(rows, cols)
        remaining = fill_in(field, mines)
        if remaining == 0:
            return str_field(field)
        else:
            if remaining == 1:
                field[rows - 3][2] = "*"
                return str_field(field)
            elif remaining == 3:
                field[rows - 3][0] = "*"
                field[rows - 3][1] = "*"
                field[rows - 3][2] = "*"
                return str_field(field)
            elif remaining == 5:
                field[rows - 3][0] = "*"
                field[rows - 3][1] = "*"
                field[rows - 3][2] = "*"
                field[rows - 2][2] = "*"
                field[rows - 1][2] = "*"
                return str_field(field)
            elif remaining == 8:
                field[rows - 3][0] = "*"
                field[rows - 3][1] = "*"
                field[rows - 3][2] = "*"
                field[rows - 2][2] = "*"
                field[rows - 1][2] = "*"
                field[rows - 1][1] = "*"
                field[rows - 2][1] = "*"
                field[rows - 2][0] = "*"
                return str_field(field)
            else:
                return "Impossible\n"

    return "Not implemented\n"

def fill_in(f, mines):
    rows = len(f)
    cols = len(f[0])

    f[rows - 1][0] = "c"

    for i in range(rows - 3):
        for j in range(cols - 1, -1, -1):
            if j == 1 and mines == 1:
                f[i + 1][cols - 1] = "*"
                return 0
            elif mines == 0:
                return mines
            else:
                f[i][j] = "*"
                mines -= 1

    for j in range(cols - 1, 2, -1):
        for i in range(rows - 3, rows):
            if i == rows - 2 and mines == 1:
                if j == 0:
                    return 1
                else:
                    f[rows - 3][j - 1] = "*"
                    return 0
            elif mines == 0:
                return mines
            else:
                f[i][j] = "*"
                mines -= 1

    return mines

def prepare_field(rows, cols):
    return [["." for i in range(cols)] for i in range(rows)]

def str_field(f):
    rows = len(f)
    cols = len(f[0])

    buf = ""

    for i in range(rows):
        for j in range(cols):
            buf += f[i][j]

        buf += "\n"

    return buf

def str_field_trans(f):
    rows = len(f)
    cols = len(f[0])
    buf = ""

    for i in range(cols):
        for j in range(rows):
            buf += f[j][i]

        buf += "\n"

    return buf

if __name__=="__main__":
    filename = sys.argv[1]
    name, ext = os.path.splitext(filename)

    with open(filename) as instream:
        with open(name + ".out", "w") as outstream:
            origout = sys.stdout
            sys.stdout = outstream
            try:
                main(instream.readlines())
            finally:
                sys.stdout = origout
