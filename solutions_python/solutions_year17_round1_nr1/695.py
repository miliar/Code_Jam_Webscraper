fileName = 'problemA'
fileName = 'problemA2'
fileName = 'A-small-attempt0'
fileName = 'A-small-attempt1'
fileName = 'A-small-attempt2'
fileName = 'A-small-attempt3'
fileName = 'A-large'

with open(fileName + '.in', 'r') as f:
    content = f.read().splitlines()

text_file = open(fileName + '.out', 'w')

content = list(reversed(content))
numTestCases = int(content.pop())

# for each test          
for testCase in range(1, numTestCases+1):
    line = content.pop().split(' ')

    R = int(line[0])
    C = int(line[1])    
    
    # initialize grid
    grid = []
    for i in range(R):
        row = content.pop()
        grid.append(list(row))

    # extend left and right as far as possible
    for i in range(R):
        
        activeChar = '?'
        if grid[i][0] == '?':
            firstCharEmpty = False
        else:
            firstCharEmpty = True

        for j in range(C):
            if grid[i][j] == '?':
                if activeChar == '?':
                    continue
                else:
                    grid[i][j] = activeChar
            else:
                activeChar = grid[i][j]
                
                # backfill any initially empty cells
                if grid[i][0] == '?':
                    grid[i][0:j] = j * activeChar
    
    # fill in blank lines downwards
#    while sum(row.count('?') for row in grid[1:R][:]) > 0:
    for times in range(25):

        for i in range(R):
            if grid[i].count('?') == C:
                # copy the one above it
                try:
                    grid[i] = grid[max(0,i-1)]
                except:
                    pass
                
    # fill in blank lines upwards
    for times in range(25):

        for i in range(R):
            if grid[i].count('?') == C:
                # copy the one below it
                try:
                    grid[i] = grid[i+1]
                except:
                    pass
                    
    # if the first line is empty, copy the one below it
    if grid[0].count('?') == C:
        print(grid)
        try:
            grid[0] = grid[1]
        except:
            pass

    # print answer
#    print("Case #{}:".format(testCase))
    text_file.write("Case #{}:\n".format(testCase))
    for row in grid:
#        print(''.join(row))
        text_file.write(''.join(row) + '\n')

text_file.close()