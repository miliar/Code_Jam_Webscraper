#!/usr/bin/python

# Google code jam 2009

import sys

def find_flow(row, col, map):
    current_alt = map[row][col]
    neighbours = [map[row - 1][col], map[row][col - 1], map[row][col + 1], map[row + 1][col]]
    n = neighbours[:]
    n.sort()
    dir = neighbours.index(n[0])
    if n[0] >= current_alt:
        return (-1, -1)
    
    if dir == 0:
        return (row - 1, col)
    if dir == 1:
        return (row, col - 1)
    if dir == 2:
        return (row, col + 1)
    if dir == 3:
        return (row + 1, col)
    return (-1, -1)

def basin(row, col, answer):
    return answer[row - 1][col - 1]
   
def is_sink(row, col):
    if row == col == -1:
        return True
    return False 

def solve(map):
    answer = []
    #print map
    current_basin = ord('a') - 1
    map = [[10000] + x + [10000] for x in map]
    cols = len(map[0])
    map = [([10000] * cols)] + map + [([10000] * cols)]
    rows = len(map)
    for i in range(rows - 2):
        x = []
        for j in range(cols - 2):
            x.append("")
        answer.append(x)
    for row in range(1 , rows - 1):
        for col in range(1, cols - 1):
            current_row = row
            current_col = col
            path = []
            while(basin(current_row, current_col, answer) == ''):
                path.append((current_row, current_col))
                (next_row, next_col) = find_flow(current_row, current_col, map)
                if is_sink(next_row, next_col):
                    current_basin = current_basin + 1
                    basin_name = chr(current_basin)
                    break
                current_row = next_row
                current_col = next_col
                basin_name = basin(current_row, current_col, answer)
            #print row, col, path

            for (row1, col1) in path:
                answer[row1 - 1][col1 - 1] = basin_name

    return answer        
    #print answer
    

def main():
    infile = file(sys.argv[1])
    lines = [x.strip() for x in infile.readlines()]
    n = int(lines[0])
    line = 1
    for i in range(n):
        #print line
        (rows, cols) = lines[line].split(" ")
        rows = int(rows)
        cols = int(cols)
        line = line + 1
        map = []
        for j in range(line, line + rows):
            row = [int(x.strip()) for x in lines[j].split(" ")]
            map.append(row)
        answer = solve(map)
        print "Case #%d:" % (i+1)
        for r in answer:
            for c in r:
                print c, 
            print
            
        line = line + rows 
    
if __name__ == "__main__":
    main()
