import sys
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

def flip(input, X, flipper):
    for i in range(0, flipper):
        input[X + i] = '+' if input[X + i] == '-' else '-'
    return input

def findIt(N, flipper):
    flips = 0
    #flipper = int(N[-1])
    #del N[-2:]
    if N[0] == '+' and N[1:] == N[:-1]:
		return 0
    else:
        #while not (N[0] == '+' and N[1:] == N[:-1]):
        for i in range(0, len(N)):
            for x in range(len(N) - flipper + 1):
                if N[0] == '+' and N[1:] == N[:-1]:
                    return flips
                
                #print N
                subList = N[x : x + flipper]
                #print subList
                if subList[0] == '-':
                    flips = flips + 1
                    N = flip(N, x, flipper)
    return -1

#                if subList[0] == '-' and subList[1:] == subList[:-1]:
#                    N = flip(N, x, flipper)
#                else:
#                    print "not combo :("
        #		for x in range(len(N) - 1, -1, -1):
        #	if N[x] == '-':
        #		N = flip(N, x + 1)
        #			print "NEXT"
        #		print N
        #		print x + 1
#		return findIt(N) + 1

def isIncreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))

def solveIt(n):
    if isIncreasing(n):
        return int(''.join(map(str,n)))
#    print n
    for i in range(len(n), -1, -1):
#        if (i != 0 and n[i-1] < n[i - 2]):
#            continue

        for j in range(int(n[i-1]), int(n[i-2]), -1):
            n[i-1] = str(j)
            if isIncreasing(n):
                return int(''.join(map(str,n)))

        for j in range(i - 1, len(n)):
            n[j] = str(9)
#        n[i - 1] = str(9)
        if n[i - 2] != '0':
            n[i - 2] = str(int(n[i - 2]) - 1)
#print n
        if isIncreasing(n):
            return int(''.join(map(str,n)))

def horizontalFill(row):
    fillWith = ''
#    Forward
    for i, item in enumerate(row):
        if item != '?':
            fillWith = item
        
        if fillWith != '' and item == '?':
            row[i] = fillWith
#    Reverse
    fillWith = ''
    for i, item in reversed(list(enumerate(row))):
        if item != '?':
            fillWith = item
            
        if fillWith != '' and item == '?':
            row[i] = fillWith
    return row

def verticalFill(grid, rows, column):
    fillWith = ''
#    Forward
    for i in range(0,rows):
        if grid[i][column] != '?':
            fillWith = grid[i][column]
        if fillWith != '' and grid[i][column] == '?':
            grid[i][column] = fillWith
#    Reverse
    fillWith = ''
    #    Forward
    for i in reversed(range(0,rows)):
        if grid[i][column] != '?':
            fillWith = grid[i][column]
        if fillWith != '' and grid[i][column] == '?':
            grid[i][column] = fillWith
    
    return grid

def solve(grid):
    if grid == []:
        return
    
#    Two digit bypass
    grid.pop(0)
    rows = len(grid)
    columns = 0
    for item in grid[0]:
        columns = columns + 1

    for i, row in enumerate(grid):
        grid[i] = horizontalFill(row)

    for i in range(0, columns):
        grid = verticalFill(grid, rows, i)
    
    return grid


results = []
firstLine = True
with open("A-large.in") as f:
    contents = f.readlines()
    grid = []
    for content in contents:
        if not firstLine:
            content = list(content.strip("\n"))
            if content[0].isdigit():
                results.append(solve(grid))
                grid = []
            grid.append(content)
#        content = (content.strip("\n")).split(' ')
#            print content
#            results.append(findIt(list(content[0]), int(content[1])))
#			results.append(solveIt(list(content.strip("\n"))))
        firstLine = False;
    f.close()
    results.append(solve(grid))


file = open("a.out", "w")
counter = 1
for item in results:
    if item == None:
        continue
    #item = "IMPOSSIBLE" if item == -1 else item
#    file.write("Case #" + str(counter) + ": " + str(item) + "\n")
    file.write("Case #" + str(counter) + ":\n")
    for row in item:
        file.write(''.join(row) + "\n")
    counter += 1

file.close()
