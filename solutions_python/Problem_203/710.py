def get_next_char(row, col_start_index):
    """
    Returns char, index where char was found in this row, was_everything_none,
    """
    for i in range(col_start_index, len(row)):
        if row[i]:
            return row[i], i, False
    else:
        return None, col_start_index, True


def is_out_of_bound_column(row, index):
    out_of_bound = True if index < 0 or index >= len(row) else False
    # print("index = ", index, "out_of_bound = ", out_of_bound)
    return out_of_bound


def is_out_of_bound_row(grid, index):
    out_of_bound = True if index < 0 or index >= len(grid) else False
    # print("index = ", index, "out_of_bound = ", out_of_bound)
    return out_of_bound


def flood_fill_row(row, ch, index):
    """
    Flood fills row wise and returns right most column index where char was filled.
    """
    # print(row, ch, index)
    # import pdb
    # pdb.set_trace()
    if is_out_of_bound_column(row, index) or (row[index] != ch and row[index] is not None):
        return -1
    elif row[index] == ch:
        return index
    else:
        row[index] = ch
        return max(
            index,
            flood_fill_row(row, ch, index - 1),
            flood_fill_row(row, ch, index + 1)
        )


def copy_from_to(grid, source_row, target_row):
    grid[target_row] = [ch for ch in grid[source_row]]


def fill(grid, rows, cols):
    last_row_filled = -1
    row_indices_unfilled = []

    for row_index in range(rows):
        # print(grid)
        # import pdb
        # pdb.set_trace()
        col_index = 0
        while col_index < cols:
            if is_out_of_bound_column(grid[row_index], col_index):
                break
            ch, col_index, no_char_found = get_next_char(grid[row_index], col_index)
            if ch:
                col_index = max(
                    flood_fill_row(grid[row_index], ch, col_index - 1),
                    col_index,
                    flood_fill_row(grid[row_index], ch, col_index + 1)
                )

                last_row_filled = row_index

            elif not ch and no_char_found:
                if last_row_filled != -1:
                    copy_from_to(grid, last_row_filled, row_index)
                else:
                    row_indices_unfilled.append(row_index)
                    break
            col_index += 1

    # Back fill rows
    for row_index in row_indices_unfilled[::-1]:
        if not is_out_of_bound_row(grid, row_index + 1):
            copy_from_to(grid, row_index + 1, row_index)
    return grid


def main():
    for test in range(int(raw_input())):
        r, c = map(int, raw_input().split())
        grid = []
        char_list = []
        head_empty_cells = node = None
        for row_num in range(r):
            row = list(raw_input())
            row = [None if ch == '?' else ch for ch in row]
            grid.append(row)
        grid = fill(grid, r, c)
        print "Case #{}: ".format(test+1)
        for row in grid:
            print ''.join(['_' if ch is None else ch for ch in row])

main()
