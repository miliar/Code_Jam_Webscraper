import sys

def expand_down(grid, row, col, initial, bounds):
    left,up,right,down = bounds
    #move in direc checking the
    for new_down in range(row + 1, len(grid)):
        for check_horz in range(left, right+1):
            if grid[new_down][check_horz] != '?':
                return new_down - 1
        for check_horz in range(left, right+1):
            grid[new_down][check_horz] = initial
    return len(grid) - 1

def expand_right(grid, row, col, initial, bounds):
    left,up,right,down = bounds
    #move in direc checking the
    for new_right in range(col + 1, len(grid[row])):
        for check_vert in range(up, down+1):
            if grid[check_vert][new_right] != '?':
                return new_right - 1
        for check_vert in range(up, down+1):
            grid[check_vert][new_right] = initial
    return len(grid[row]) - 1

def expand_up(grid, row, col, initial, bounds):
    left,up,right,down = bounds
    #move in direc checking the
    for new_up in range(row-1, -1, -1):
        for check_horz in range(left, right+1):
            if grid[new_up][check_horz] != '?':
                return new_up + 1
        for check_horz in range(left, right+1):
            grid[new_up][check_horz] = initial
    return 0

def expand_left(grid, row, col, initial, bounds):
    left,up,right,down = bounds
    #move in direc checking the
    for new_left in range(col-1, -1, -1):
        for check_vert in range(up, down+1):
            if grid[check_vert][new_left] != '?':
                return new_left + 1
        for check_vert in range(up, down+1):
            grid[check_vert][new_left] = initial
    return 0
        

def fill(grid):
    visited = set()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cell = grid[row][col]
            if cell != '?' and cell not in visited:
                visited.add(cell)
                cur_bounds=[col,row,col,row]
                cur_bounds[0]=expand_left(grid, row, col, cell, cur_bounds)
                cur_bounds[1]=expand_up(grid, row, col, cell, cur_bounds)
                cur_bounds[2]=expand_right(grid, row, col, cell, cur_bounds)
                cur_bounds[3]=expand_down(grid, row, col, cell, cur_bounds)
                

def solve(in_file, out_file):
    neg = "IMPOSSIBLE"
    num_cases = int(in_file.readline().strip())
    for case in range(1, num_cases + 1):
        #Read in data
        height, width = (int(val) for val in in_file.readline().strip().split())
        grid = []
        for _ in range(height):
            row = list(in_file.readline().strip())
            grid.append(row)
        fill(grid)
        #Call func for solution
        out_file.write("Case #{}:\n".format(case))
        for row in grid:
            out_file.write("{}\n".format("".join(row)))

if __name__ == '__main__':
    from_file = True
    alt_out = False
    
    if from_file:
        path = 'Data\\'
        #name = 'A-sample'
        #name = 'A-small-attempt3'
        name = 'A-large'
        file_input = open(path + name + '.in', 'r')
        out_full_name = path + name +'.out'
        if alt_out:
            out_full_name = path + name + "naive" +'.out'            
        file_output = open(out_full_name,'w')
        solve(file_input, file_output)
        file_input.close()
        file_output.close()
    else:
        solve(sys.stdin, sys.stdout)
        
        
