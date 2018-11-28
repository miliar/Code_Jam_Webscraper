#!/usr/bin/env python


def doable(grid, nx, ny):
    #iterate over each grid element:
    for x in range(nx):
        for y in range(ny):
            val = grid[x][y]  #value of the element
            
            #test vertical:
            flag = True            
            for xx in range(nx):
                if val < grid[xx][y]:
                    flag = False
                    break
            if flag is True:
                continue
            
            #test horizontal:        
            flag = True        
            for yy in range(ny):
                if val < grid[x][yy]:
                    flag = False
                    break
            
            if flag is False:
                return "NO"
                
    return "YES"




# grid = [   
#          [3, 1, 3, 3],
#          [2, 1, 2, 2],
#          [2, 1, 2, 2], 
#          [3, 1, 3, 3],
#        ]
       
grid = [
          [1, 3, 3],
          [1, 4, 3],
          [1, 3, 3],
          [1, 3, 3]
        ]

def parseGrid(handle):
    line = handle.readline()
    lspl = line.split()
    x = int(lspl[0])
    y = int(lspl[1])
    
    grid = []
    
    for l in range(x):
        line = handle.readline()
        lspl = line.split()
        xline = [int(i) for i in lspl ]
        grid.append(xline)
    return grid    
        


if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    f = open(filename, "r")
    
    n = int(f.readline())
    for i in range(n):
        grid = parseGrid(f)
        print "Case #%i: %s"%( i+1 ,  doable(grid, len(grid), len(grid[0])) )
    
    





