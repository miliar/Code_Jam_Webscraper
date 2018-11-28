def solution(grid, r, c):
    for r_i in range(r):
        row_i = grid[r_i]
        last_char_i = 0
        last_char = None
        first_char = None

        for c_i in range(c):
            #print(c_i, row_i)
            if row_i[c_i] != "?":
                if first_char is None:
                    first_char = row_i[c_i] 
                    last_char = first_char
                #print("vars:", last_char_i, c_i, (c_i - last_char_i))
                for c_i_2 in range(last_char_i, c_i):
                    row_i[c_i_2] = row_i[c_i]
                last_char_i = c_i + 1
                last_char = row_i[c_i]
        if first_char is not None:
            for c_i_3 in range(last_char_i, c):
                row_i[c_i_3] = last_char
    first_line = None
    last_line = None
    last_line_i = 0
    for r_i in range(r):
        #print(c_i, row_i)
        if grid[r_i][0] != "?":
            if first_line is None:
                first_line = grid[r_i] 
                last_line = first_line
            #print("vars:", last_line_i, c_i, (c_i - last_line_i))
            for r_i_2 in range(last_line_i, r_i):
                grid[r_i_2] = grid[r_i]
            last_line_i = r_i + 1
            last_line = grid[r_i]
    for r_i_3 in range(last_line_i, r):
        grid[r_i_3] = last_line




    return grid



# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(input())  # read a line with a single integer
for i in range(1, total + 1):
    r_t, c_t = input().split(" ")  # read a list of integers, 2 in this case
    r_t = int(r_t)
    c_t = int(c_t)
    grid = []
    for r_i in range(r_t):
        grid.append(list(input()))

    result = solution( grid, r_t, c_t)
    print("Case #{}:".format(i))
    for index in range(r_t):
        grid_row = result[index]
        row_s = ""
        for char in grid_row:
            row_s += char
        print(row_s)
  # check out .format's specificatin for more formatting options