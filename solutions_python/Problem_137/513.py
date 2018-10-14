import sys

f = open('D:\Users\john\My Documents\Google Code Jam 2014\mine_small.txt','r+')
g = open('D:\Users\john\My Documents\Google Code Jam 2014\mine_small_answer.txt','w+')

test_cases = int(f.readline())

for t in range(test_cases):
    R, C, M = f.readline().split()
    R, C, M = int(R), int(C), int(M)
    grid = []
    
    safe_spaces = (R * C) - M
    left_to_fill = safe_spaces
    impossible = False
    
    for y in range(R):
        row = []
        for x in range(C):
            row.append('*')
        grid.append(row)
            
    grid[0][0] = 'c'
    left_to_fill -= 1
    #print('t:',t)
    if R == 1:
        temp_col = 1
        while left_to_fill > 0:
            grid[0][temp_col] = '.'
            temp_col += 1
            left_to_fill -= 1
    elif C == 1:
        temp_row = 1
        while left_to_fill > 0:
            grid[temp_row][0] = '.'
            temp_row += 1
            left_to_fill -= 1
    elif R == 2:
        if safe_spaces == 1:
            pass
        elif safe_spaces % 2:
            g.write('Case #'+str(t+1)+':\n')
            g.write('Impossible\n')
            impossible = True
        elif safe_spaces < 4:
            g.write('Case #'+str(t+1)+':\n')
            g.write('Impossible\n')
            impossible = True
        else:
            grid[1][0] = '.'
            left_to_fill -= 1
            temp_col = 1
            while left_to_fill > 0:
                grid[0][temp_col] = '.'
                grid[1][temp_col] = '.'
                temp_col += 1
                left_to_fill -= 2
    elif C == 2:
        if safe_spaces == 1:
            pass
        elif safe_spaces % 2:
            g.write('Case #'+str(t+1)+':\n')
            g.write('Impossible\n')
            impossible = True
        elif safe_spaces < 4:
            g.write('Case #'+str(t+1)+':\n')
            g.write('Impossible\n')
            impossible = True
        else:
            grid[0][1] = '.'
            left_to_fill -= 1
            temp_row = 1
            while left_to_fill > 0:
                grid[temp_row][0] = '.'
                grid[temp_row][1] = '.'
                temp_row += 1
                left_to_fill -= 2
    else:
        if safe_spaces == 1:
            pass
        elif safe_spaces < 4:
            g.write('Case #'+str(t+1)+':\n')
            g.write('Impossible\n')
            impossible = True
        elif ((safe_spaces % 2) and (safe_spaces < 8)):
            g.write('Case #'+str(t+1)+':\n')
            g.write('Impossible\n')
            impossible = True
            
        # Odd safe spaces
        elif safe_spaces % 2:
            grid[0][1] = '.'
            left_to_fill -= 1
            done = False
            
            for x in range(len(grid[0])//2):
                for y in range(len(grid)):
                    if (x, y) != (0, 0):
                        if left_to_fill <= 0:
                            done = True
                            break
                        elif left_to_fill == 1:
                            if ((y == (len(grid) - 1)) and (x == 0)):
                                grid[y-1][x * 2] = '*'
                                grid[y-1][x * 2 + 1] = '*'
                                grid[0][(x + 1) * 2] = '.'
                                grid[1][(x + 1) * 2] = '.'
                                grid[2][(x + 1) * 2] = '.'
                                left_to_fill -= 1
                                done = True
                                break
                            else:
                                grid[y][x * 2] = '.'
                                left_to_fill -= 1
                                done = True
                                break
                        elif ((left_to_fill == 3) and (y == (len(grid) - 1))):
                            if (((x * 2) == (len(grid[0]) - 3)) and (x != 0)):
                                grid[y][x * 2] = '.'
                                left_to_fill -= 1
                                done = True
                                break
                            else:
                                grid[0][(x + 1) * 2] = '.'
                                grid[1][(x + 1) * 2] = '.'
                                grid[2][(x + 1) * 2] = '.'
                                left_to_fill -= 3
                                done = True
                                break
                        elif ((left_to_fill == 5) and (y == (len(grid) - 1))):
                            grid[y][x * 2] = '.'
                            grid[y][x * 2 + 1] = '.'
                            grid[0][(x + 1) * 2] = '.'
                            grid[1][(x + 1) * 2] = '.'
                            grid[2][(x + 1) * 2] = '.'
                            left_to_fill -= 5
                            done = True
                            break
                            
                        grid[y][x * 2] = '.'
                        grid[y][x * 2 + 1] = '.'
                        left_to_fill -= 2
                
                if done:
                    break
            
            # Fill last column
            if len(grid[0]) % 2:
                while left_to_fill > 0:
                    grid[left_to_fill - 1][-1] = '.'
                    left_to_fill -= 1
                    
        # Even safe spaces
        else:
            grid[0][1] = '.'
            left_to_fill -= 1
            done = False
            
            for x in range(len(grid[0])//2):
                for y in range(len(grid)):
                    if (x, y) != (0, 0):
                        if left_to_fill <= 0:
                            done = True
                            break
                        elif ((left_to_fill == 4) and (y == (len(grid) - 1))):
                            if (x * 2) == (len(grid[0]) - 3):
                                pass
                            else:
                                break
                                
                        grid[y][x * 2] = '.'
                        grid[y][x * 2 + 1] = '.'
                        left_to_fill -= 2
                
                if done:
                    break
            
            # Fill last column
            if len(grid[0]) % 2:
                while left_to_fill > 0:
                    grid[left_to_fill - 1][-1] = '.'
                    left_to_fill -= 1
                    
    if not impossible:
        g.write('Case #'+str(t+1)+':\n')
        for y in grid:
            for x in y:
                g.write(x)
            g.write('\n')

f.close()
g.close()