'''
Created on 22.05.2011

@author: LordB
'''

inFile = open('A-large.in', 'r')
outFile = open('output_Problem_1_large.txt', 'w')

nrOfCases = int( inFile.readline() )


for caseNr in range(1, nrOfCases+1):
    print('Working on #', caseNr)
    tmp = inFile.readline().replace('\n','').split(" ")
    height = int(tmp[0])
    width = int(tmp[1])
    grid = []
    
    for h in range(height):
        tmp = inFile.readline().replace('\n','').replace(' ','')
        tmp2 = []
        for t in tmp:
            tmp2.append(t)
        grid.append(tmp2)
    
    impossible = False
    print('Grid:    ',grid)
    g = 0
    
    for line in grid:
        if(impossible): break
        
        for i in range(len(line)):
            if(line[i] == '#'):
                if(i == len(line)-1 or line[i+1] != '#'):
                    impossible = True
                    break
                elif(g == len(grid)-1 or grid[g+1][i] != '#' or grid[g+1][i+1] != '#'):
                    impossible = True
                    break
                else:
                    line[i] = '/'
                    line[i+1] = '\\'
                    #line[i+1] = line[i+1][:]
                    grid[g+1][i] = '\\'
                    #grid[g+1][i] = grid[g+1][i][:0]
                    grid[g+1][i+1] = '/'
        g += 1
    print('nachher: ',grid)
    if(impossible):
        outFile.write( ('Case #{}:\nImpossible\n'.format(caseNr)))
    else:
        outFile.write( ('Case #{}:\n'.format(caseNr)))
        for line in grid:
            for c in line:
                outFile.write( ('{}'.format(c)))
            outFile.write( ('\n'))
    
         
    
#outFile.write( ('Case #{}: {}\n'.format(caseNr, output)).replace('\'', '') )