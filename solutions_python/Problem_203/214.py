def copy_row(grid, src, dest):
    for idx, char in enumerate(grid[src]):
        grid[dest][idx] = char

def process_row(row):
    previous_letter = None
    unmatched_qm = 0
    for idx, char in enumerate(row):
        if char == '?':
            if previous_letter is not None:
                row[idx] = previous_letter
            else:
                unmatched_qm += 1
        else:
            previous_letter = char
            for k in range(unmatched_qm):
                row[idx-k-1] = previous_letter
            unmatched_qm = 0
    return unmatched_qm == 0

def solve(grid):
    prev_nonempty_idx = None
    empty_rows = 0
    for idx, row in enumerate(grid):
        filled = process_row(row)
        if filled:
            prev_nonempty_idx = idx
            for k in range(empty_rows):
                copy_row(grid, idx, idx-k-1)
            empty_rows = 0
        else:
            if prev_nonempty_idx is not None:
                copy_row(grid, prev_nonempty_idx, idx)
            else:
                empty_rows += 1
    return grid # just for ease of use

def load_grid(row_no):
    grid = [list(input()) for _ in range(row_no)]
    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))


def main():
    case_count = int(input())

    for case_no in range(1, case_count + 1):
        _rows, _ = input().split()
        grid = load_grid(int(_rows))
        print('Case #{0}:'.format(case_no))
        print_grid(solve(grid))

if __name__ == '__main__':
    main()
