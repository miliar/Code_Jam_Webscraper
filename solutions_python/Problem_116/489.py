#!/usr/bin/env python

def lines(grid):
    return ([row for row in grid] +  # rows
            [[row[x] for row in grid] for x in range(4)] +  #columns
            [[grid[i][i] for i in range(4)]] +  # TL->BR diagonal
            [[grid[i][-(i+1)] for i in range(4)]])  # TR->BL diagonal

def line_winner(line):
    if all([square in ["X", "T"] for square in line]):  # all squares are X or T
        return "X"
    elif all([square in ["O", "T"] for square in line]):  # all squares are O or T
        return "O"

def grid_full(grid):
    return not "." in [square for row in grid for square in row]

def test_grid(grid):
    won_lines = [line_winner(line) for line in lines(grid) if line_winner(line)]
    if len(won_lines) >= 1:  # 2 intersecting lines can be won together
        return "{0} won".format(won_lines[0])  # but only by the same player, so this is still ok
    elif grid_full(grid):
        return "Draw"
    else:
        return "Game has not completed"

def main():
    import sys

    num_test_cases = int(next(sys.stdin).strip())
    for i in range(num_test_cases):
        grid = [list(next(sys.stdin).strip()) for j in range(4)]
        try:
            next(sys.stdin)  # try to consume the blank line
        except StopIteration:
            pass  # ignore the end-of-file if there is no blank line
        sys.stdout.write("Case #{0}: {1}\n".format(i+1, test_grid(grid)))


if __name__ == "__main__":
    main()
