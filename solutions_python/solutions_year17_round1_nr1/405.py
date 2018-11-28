import sys
import typing
import argparse

def slice_cake(cake):
    """Slice the cake.

    The cake should be a nest list giving the matrix of initials.  And it shall
    be mutated.
    """

    n_rows = len(cake)
    n_cols = len(cake[0])
    for row in range(n_rows):
        for col in range(n_cols):
            curr = cake[row][col]
            if curr[0] == '?' or curr[1]:
                continue

            left, right = col, col + 1
            top, bott = row, row + 1

            while left != 0 and cake[row][left - 1][0] == '?':
                left -= 1
            while right != n_cols and cake[row][right][0] == '?':
                right += 1

            while top != 0 and all(
                    i[0] == '?' for i in cake[top - 1][left:right]
            ):
                top -= 1
            while bott != n_rows and all(
                    i[0] == '?' for i in cake[bott][left:right]
            ):
                bott += 1

            for i in range(top, bott):
                for j in range(left, right):
                    cake[i][j] = (curr[0], True)

            continue
        continue

    return


def main():
    """The main driver."""

    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'), default=sys.stdin)
    args = parser.parse_args()
    inp = args.input

    n_cases = int(inp.readline())
    for i in range(n_cases):
        line = inp.readline().split()
        n_rows = int(line[0])
        cake = []
        for j in range(n_rows):
            cake.append([
                (i, False) for i in
                inp.readline().strip()
            ])
            continue

        slice_cake(cake)
        print('Case #{}:'.format(i + 1))
        for j in cake:
            print(''.join(k[0] for k in j))

        continue


if __name__ == '__main__':
    main()
