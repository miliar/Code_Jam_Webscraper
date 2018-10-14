from numpy.matlib import zeros
import sys


SIZE = 4
ORD_T = ord('T')


def slice_has_only(arr, sx, sy, dx, dy, symbol):
    result = True
    i = sx
    j = sy

    while i < SIZE and j < SIZE:
        x = arr[i, j]
        if x != symbol and x != ORD_T:
            result = False
            break
        i += dx
        j += dy

    return result


def won(arr, symbol):
    result = False

    i = 0
    for i in range(SIZE):
        result = slice_has_only(arr, i, 0, 0, 1, symbol) or slice_has_only(arr, 0, i, 1, 0, symbol)
        if result:
            break

    if not result:
        result = slice_has_only(arr, 0, 0, 1, 1, symbol) or slice_has_only(arr, SIZE - 1, 0, -1, 1, symbol)

    return result


def game_state(arr):
    if won(arr, ord('X')):
        return 'X won'
    elif won(arr, ord('O')):
        return 'O won'
    else:
        return 'Draw'


if __name__ == "__main__":
    if len(sys.argv) == 1:
        f_in = open("in.txt", "rt")
        f_out = sys.stdout
    else:
        f_in = open(sys.argv[1], "rt")
        f_out = open("out.txt", "wt")

    case_num = int(f_in.readline())

    for c in range(case_num):
        arr = zeros((SIZE, SIZE,), dtype=int)
        result = ''
        has_empty = False
        for i in range(SIZE):
            line = f_in.readline().strip()
            for j in range(SIZE):
                arr[i, j] = ord(line[j])
                if line[j] == '.':
                    has_empty = True
        f_in.readline()

        result = game_state(arr)
        if result == 'Draw' and has_empty:
            result = 'Game has not completed'

        f_out.write("Case #%d: %s\n" % (c + 1, result))
    f_in.close()
    f_out.close()
