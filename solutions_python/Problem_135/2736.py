def determine(case):
    row1 = case[0] - 1
    grid1 = case[1]
    row2 = case[2] - 1
    grid2 = case[3]
    
    intersection = []
    for item1 in grid1[row1]:
        for item2 in grid2[row2]:
            if item1 == item2:
                intersection.append(item1)
    
    if len(intersection) == 0:
        return 'Volunteer cheated!'
    elif len(intersection) == 1:
        return str(intersection[0])
    else:
        return 'Bad magician!'
            
def processinput(filename):
    f = open(filename, 'r')
    cases = int(f.readline())
    
    output = []
    for i in range(cases):
        row1 = int(f.readline())
        grid1 = []
        for i in range(4):
            row = f.readline().split()
            grid1.append([int(x) for x in row])
            
        row2 = int(f.readline())
        grid2 = []
        for i in range(4):
            row = f.readline().split()
            grid2.append([int(x) for x in row])
            
        output.append([row1, grid1, row2, grid2])
    
    f.close()
    
    return output
    
def output(infile, outfile):
    f = open(outfile, 'w')
    
    counter = 0
    input = processinput(infile)
    for case in input:
        counter += 1
        f.write('Case #' + str(counter) + ': ' + determine(case) + '\n')
        
    f.close()
    
output('A-small-attempt0.in', 'A-small-attempt0.out')