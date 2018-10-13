
def get_cases():

    data = open("input.txt").read().splitlines()
    count = int(data.pop(0))
    cases = []
    
    for i in xrange(count):

        count = int(data.pop(0))
        rects = []
        for i in xrange(count):
            rects.append(map(int, data.pop(0).split()))

        
            
        cases.append(rects)

    return cases

def addwidth(grid, toadd):

    grid = [ line + '0'*toadd for line in grid ]

    return grid


def addheight(grid, toadd):

    grid += [ '0'*len(grid[0]) for i in xrange(toadd) ]

    return grid

def addrect(grid, rect):

    x1, y1, x2, y2 = rect

    if x2 > len(grid[0]):
        grid = addwidth(grid, x2 - len(grid[0]))

    if y2 > len(grid):
        grid = addheight(grid, y2 - len(grid))
    

    for i in xrange(y1 - 1, y2):

        line = grid[i]
        grid[i] = line[:x1 - 1] + '1' * (x2 - x1 + 1) + line[x2:]


    return grid

def makegrid(rects):

    grid = [""]
    for rect in rects:
        grid = addrect(grid, rect)

    return grid

def tick(grid):

    newgrid = []
    rowlen = len(grid[0])

    for i in xrange(len(grid)):

        row = int(grid[i], 2)
        
        prevrow = int(grid[i - 1], 2) if i > 0 else 0b0

        shiftrow = row >> 1


        #if brought to life, or stay alive
        row = (prevrow & shiftrow) | ((shiftrow | prevrow) & row)

        row = bin(row)[2:]
        row = ('0'*rowlen + row)[-rowlen:]

        newgrid.append(row)

    return newgrid
        

def solve(case):

    grid = makegrid(case)
    print "grid:\n" + '\n'.join(grid)
    solved = False

    seconds = 0
    while not solved:
        seconds += 1
        grid = tick(grid)

        solved = True
        for line in grid:
            if '1' in line:
                solved = False
                break

    return seconds

if __name__ == "__main__":

    cases = get_cases()
    output = ""
    for i, case in enumerate(cases):

        result = "Case #{0}: {1}\n".format(i + 1, solve(case))
        print "done", i + 1, "of", len(cases)
        output += result

    open("output.txt", "w").write(output)
    print "output:\n" + output
    print "done all!"
    
