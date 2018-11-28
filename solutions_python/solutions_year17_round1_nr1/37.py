IN_FILE = "A_large.in"

infile = open(IN_FILE)
out = open("A.out","w")

def output(string):
    print string.rstrip("\n")
    out.write(string)

cases = int(infile.readline())

def process(row):
    for i in range(len(row)):
        if row[i] == "?":
            for j in range(i,len(row)):
                if row[j] != "?":
                    row[i] = row[j]
                    break
            else:
                for j in reversed(range(0,i)):
                    if row[j] != "?":
                        row[i] = row[j]
                        break
    return row

for case in range(cases):
    print "\n"
    output("Case #%i: " %(case+1))
    
    r,c = map(int,infile.readline().split())
    grid = []
    for _ in range(r):
        grid.append(list(infile.readline().strip()))
    #print grid
    
    none = []
    for y in range(len(grid)):
        if grid[y].count("?") < c:
            #print grid[y]
            grid[y] = process(grid[y])
            #print grid[y]
            
            
    for y in range(len(grid)):
        if grid[y].count("?") == c:
            for j in range(y,len(grid)):
                if grid[j].count("?") < c:
                    grid[y] = grid[j]
                    break
            else:
                for j in reversed(range(0,y)):
                    if grid[j].count("?") < c:
                        grid[y] = grid[j]
                        break
            
    #print grid
    
    for row in grid:
        output("\n")
        output("".join(row))
    output("\n")    
 
 
#fix line endings in input file   
infile.close()
infile = open(IN_FILE)
contents = infile.read()
infile.close()
infile = open(IN_FILE,"w")
infile.write(contents)
infile.close()
out.close()