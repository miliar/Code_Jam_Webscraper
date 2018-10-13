in_file = open('test.in','r')
t = int(in_file.readline().strip())



results = []
for case in range(t):
    r,c = map(int,in_file.readline().strip().split())
    grid = []
    result = 'Case #{}:\n'.format(case+1)
    
    initials = set()
    
    for row in range(r):
        line = in_file.readline().strip()
        grid.append(list(line))
        for col in range(c):
            if line[col] != '?':
                initials.add((row,col,line[col]))
        
    
    for row,col,val in initials:
        up =0
        down =0
        left = 0
        right = 0
        #check up:
        while True:
            if row-up-1>=0:
                if grid[row-up-1][col] == '?':
                    grid[row-up-1][col] = val
                    up+=1
                else:
                    break
            else:
                break
        #check down:
        while True:
            if row+down+1<r:
                if grid[row+down+1][col] == '?':
                    grid[row+down+1][col] = val
                    down+=1
                else:
                    break
            else:
                break
        #check left:
        while True:
            if col-left - 1 >= 0:
                is_clr = True
                for a in range(row-up,row+down+1):
                    if grid[a][col-left-1] != '?':
                        is_clr = False
                if not is_clr:
                    break
                for a in range(row-up,row+down+1):
                    grid[a][col-left-1] = val
                left+=1
            else:
                break
        #check right:
        while True:
            if col+right + 1 < c:
                is_clr = True
                for a in range(row-up,row+down+1):
                    if grid[a][col+right+1] != '?':
                        is_clr = False
                if not is_clr:
                    break
                for a in range(row-up,row+down+1):
                    grid[a][col+right+1] = val
                right+=1
            else:
                break
    
    for row in grid:
        for col in row:
            result+=col
        result+='\n'
    results.append(result)
    
in_file.close()




out_file = open('test.out','w')
for result in results:
    out_file.write(result)
    print(result)
out_file.close()




