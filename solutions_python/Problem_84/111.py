import sys

def Solve(tiles, Y, X):
    currentX = 0
    currentY = 0
    for line in tiles:
        currentX = 0
        for tile in line:
            if tile == 1:
                if currentX < X-1 and line[currentX+1] == 1 and currentY < Y-1 and tiles[currentY+1][currentX] == 1 and tiles[currentY+1][currentX+1] == 1:
                    tiles[currentY][currentX] = 2
                    tiles[currentY+1][currentX] = 3                   
                    tiles[currentY][currentX+1] = 3
                    tiles[currentY+1][currentX+1] =2
                else:
                    return -1   
            currentX += 1
        currentY+=1
    return tiles

f = open('a.in')

T = int(f.readline())
for t in range(T):
    line = f.readline().split()
    #print line
    R, C = map(int, line)
    tiles = []
    tiles_numbers = []
    for r in range(R):
        line = f.readline().split()
        tiles += [line[0]]
    
    for line in tiles:
        thisline = []
        for tile in line:
            if tile == "#":
                thisline.append(1)
            else:
                thisline.append(0)
        tiles_numbers.append(thisline)
                
    #print tiles_numbers      
    result = Solve(tiles_numbers, R, C)
    print "Case #%d:" % (t+1)
    if result == -1:
        print "Impossible"
    else:        
        for line in result:
            for tile in line:
                if tile == 0:
                    sys.stdout.write(".")
                if tile == 2:
                    sys.stdout.write("/")
                if tile == 3:
                    sys.stdout.write("\\")
            
            sys.stdout.write("\n")   
                
                
                
                
                