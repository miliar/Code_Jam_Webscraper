def full_test(grid):
    for i in range(len(grid)-1):
        for j in range(len(grid[0])-1):
            if grid[i][j] == '#' and grid[i][j+1] == '#' and grid[i+1][j] == '#' and grid[i+1][j+1] == '#':
                grid[i][j] = '/'
                grid[i][j+1] = '\\'
                grid[i+1][j] = '\\'
                grid[i+1][j+1] = '/'
                return True
    return False

def true_alg(grid):

    print(grid)
    print(" ")

    rotated_grid = [ [ grid[j][i] for j in range(len(grid)) ] for i in range(len(grid[0])) ]

    print(rotated_grid)

    for line in grid:
        if (line.count('#') % 2 != 0):
            return None

    for line in rotated_grid:
        if (line.count('#') % 2 != 0):
            return None
    
    while full_test(grid):
        pass

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                return None
            
    return grid
    
def alg(grid):
    result = true_alg(grid)
    if result == None:
        return 'Impossible'
    else:
        return '\n'.join(["".join(line) for line in result])

if __name__ == '__main__':
    fname = "A"
#    f = open(fname+".in.txt", "r")
#    f = open("/home/lawford/Desktop/"+fname+"-small-attempt1.in")
    f = open("/home/lawford/Desktop/"+fname+"-large.in")
    num_cases = int(f.readline().split(' ')[0])
    cnt=1
    fout = open(fname+".out.txt", "w")

# 1-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        result = alg(piece1.split(' ')[1:])
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()


    for case in range(num_cases):
        (r,c) = f.readline().split(' ')
        r = int(r)
        c = int(c)

        grid = []
        for i in range(r):
            grid.append(list(f.readline().strip()))

        result = [ alg(grid) ]
            
        fout.write("Case #"+str(cnt)+":\n"+"".join(map(str, result))+"\n")
#        piece1 = f.readline()
        

# 2-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        num_lines = int(piece1)
#        lines = []
#        for i in range(0, num_lines*2-1):
##            [s,e] = map(int, f.readline().split(" "))
#            line = f.readline().strip()
#            print(line)
#            lines.append( map(int, line.split(" ")) )
#        result = alg(lines)
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()

        cnt = cnt+1
    fout.write("\n")
    fout.close()
    f.close()
