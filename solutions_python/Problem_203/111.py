def process():
    t = int(input())
    for i in range(1, t + 1):
        r, c = [int(s) for s in input().split(" ")]
        rows = []
        for j in range(r):
            rows.append([c for c in input()])
        out_rows = process_rows(rows)
        print("Case #{}:".format(i))
        for arr in out_rows:
            print("".join(arr))

def process_rows(rows):
    for row in range(len(rows)):
        for col, char in enumerate(rows[row]):
            if char != '?':
                copy_down(char, rows, row, col)
                copy_up(char, rows, row, col)

    for row in range(len(rows)):
        for col, char in enumerate(rows[row]):
            if char != '?':
                copy_left(char, rows, row, col)
                copy_right(char, rows, row, col)
    return rows

def copy_down(char, rows, curr_row, curr_col):
    for r in range(curr_row+1, len(rows)):
        if rows[r][curr_col] == '?':
            rows[r][curr_col] = char
        else:
            break

def copy_up(char, rows, curr_row, curr_col):
    for r in range(curr_row-1, -1, -1):
        if rows[r][curr_col] == '?':
            rows[r][curr_col] = char
        else:
            break


def copy_left(char, rows, curr_row, curr_col):
    for c in range(curr_col-1, -1, -1):
        if rows[curr_row][c] == '?':
            rows[curr_row][c] = char
        else:
            break


def copy_right(char, rows, curr_row, curr_col):
    for c in range(curr_col+1, len(rows[0])):
        if rows[curr_row][c] == '?':
            rows[curr_row][c] = char
        else:
            break

if __name__ == "__main__":
    process()
