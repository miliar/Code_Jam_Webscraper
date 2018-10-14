def solve_case(num_rows, num_columns, grid):
    donate_rows = 0
    for row_index in range(num_rows):
        row = grid[row_index]
        
        initialed_cells = 0
        for cell in row:
            if cell != '?':
                initialed_cells += 1

        if initialed_cells == 0:
            donate_rows += 1
        else:
            # Split cake amongst initials in row
            
            # Find first initial
            first_initial = ''
            for col in range(num_columns):
                if row[col] != '?':
                    first_initial = row[col]
                    break
            # Fill in rest
            initial = first_initial
            for col in range(num_columns):
                if row[col] == '?':
                    row[col] = initial
                else:
                    initial = row[col]
            
            if donate_rows > 0:
                # copy up
                for donate_num in range(donate_rows):
                    donate_row = row_index - donate_num - 1
                    for col in range(num_columns):
                        grid[donate_row][col] = grid[row_index][col]
                        
            donate_rows = 0
    
    # special case at end, fill from top down
    if donate_rows > 0:
        for donate_num in range(donate_rows):
            donate_row = -donate_num - 1
            for col in range(num_columns):
                grid[donate_row][col] = grid[-donate_rows - 1][col]
    
    return grid

num_cases = int(input())

for case in range(num_cases):
    case_string = input()
    num_rows = int(case_string.split(' ')[0])
    num_columns = int(case_string.split(' ')[1])

    grid = []
    
    for i in range(num_rows):
        row = input()
        row_list = list(row)
        if len(row_list) != num_columns:
            print(("ERROR: incorrect number of row entries, expected " + str(num_columns) +
                  ", got " + str(len(row_list))))
        grid.append(list(row))

    result = solve_case(num_rows, num_columns, grid)
        
    print("Case #" + str(case + 1) + ":")
    for row in result:
        print(''.join(row))