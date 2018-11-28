
def solve(grid):
    r_len = len(grid)
    c_len = len(grid[0])
    filled_rows = [0] * r_len
    for r, row in enumerate(grid):
        if row.count('?') != c_len:
            filled_rows[r] = 1
    # need to fill all the empty rows with copies
    while sum(filled_rows) != r_len:
        for r in range(r_len):
            if filled_rows[r]:
                top_r = r - 1
                bot_r = r + 1
                if top_r >= 0 and not filled_rows[top_r]:
                    grid[top_r] = list(grid[r])
                    filled_rows[top_r] = 1
                if bot_r < r_len and not filled_rows[bot_r]:
                    grid[bot_r] = list(grid[r])
                    filled_rows[bot_r] = 1
    # Now, for every row, we need to extend until filled
    for ri, row in enumerate(grid):
        new_row = list(row)
        letters = ''.join(row).replace('?', '')
        curr_letter = 0
        for c in range(c_len):
            if new_row[c] == '?':
                new_row[c] = letters[curr_letter]
            elif curr_letter < len(letters) - 1 and new_row[c] == letters[curr_letter + 1]:
                curr_letter += 1
        grid[ri] = list(new_row)
    return grid

def pretty_print(grid):
    for row in grid:
        print ''.join(row)

t = input()

for i in range(1, t + 1):
    r, c = map(int, raw_input().strip().split())
    grid = []
    for _ in range(r):
        grid.append(list(raw_input().strip()))
    new_grid = solve(grid)
    print 'Case #{}:'.format(i)
    pretty_print(new_grid)
