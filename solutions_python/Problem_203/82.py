import sys

def solve(R, C, grid):
    print R
    print C
    print grid
    for i in range(0, R):
        cur_char = '?'
        first_char_pos = -1
        for j in range(0, C):
            if grid[i][j] == '?' and cur_char == '?':
                continue
            elif grid[i][j] == '?':
                grid[i][j] = cur_char
            else:
                cur_char = grid[i][j]
        for j in range(C-1, -1, -1):
            if grid[i][j] == '?' and cur_char == '?':
                continue
            elif grid[i][j] == '?':
                grid[i][j] = cur_char
            else:
                cur_char = grid[i][j]

    for i in range(0, C):
        cur_char = '?'
        first_char_pos = -1
        for j in range(0, R):
            if grid[j][i] == '?' and cur_char == '?':
                continue
            elif grid[j][i] == '?':
                grid[j][i] = cur_char
            else:
                cur_char = grid[j][i]
        for j in range(R-1, -1, -1):
            if grid[j][i] == '?' and cur_char == '?':
                continue
            elif grid[j][i] == '?':
                grid[j][i] = cur_char
            else:
                cur_char = grid[j][i]        
    print grid
    return grid

#in_file = open("input.txt", 'r')
#in_file = open("A-small-attempt0.in", 'r')
in_file = open("A-large.in", 'r')

out_file = open("output.txt", 'w')
    
size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip().split()
    R = int(line[0])
    C = int(line[1])
    grid = []
    for i in range(0, R):
        grid.append([])
        line = in_file.readline().strip()
        for j in range(0, C):
            grid[i].append(line[j])
    
        
    sol = solve(R, C, grid)

    answer = "Case #" + str(case) + ":\n"
    for i in range(0, R):
        for j in range(0, C):
            answer += grid[i][j]
        answer +="\n"
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

