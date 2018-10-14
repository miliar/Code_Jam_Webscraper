'''
Jirasak Chirathivat
'''
import os
import os.path
import sys
import math

sys.setrecursionlimit(1000000000)

#### CHANGE HERE ####
#globals()['happy'] = {}
filename = 'A-large.in'

#### CHANGE HERE ####

def solve(tiles, ROW, COLUMN):
    for i in range(ROW):
        row = tiles[i]
        for j in range(COLUMN):
            if tiles[i][j] == '#':
                if i == ROW - 1 or j == COLUMN-1:
                    return '\nImpossible'
                if tiles[i+1][j+1] == '#' and tiles[i+1][j] == '#'  and tiles[i][j+1] == '#':
                    tiles[i][j] = '/'
                    tiles[i][j+1] = '\\'
                    tiles[i+1][j] = '\\'
                    tiles[i+1][j+1] = '/'
                else:
                    return '\nImpossible'
    #print [''.join(y) for y in tiles] 
    return '\n' + '\n'.join([''.join(y) for y in tiles] )


if __name__ == '__main__':    
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('aout.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    line = 1
    
    #happy = createHappy()
    
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        row, col = [int(x) for x in aread[line].split(' ')]
        tiles = [list(x) for x in aread[line+1:line+1+row]]
        line += 1 + row
        #### CHANGE HERE

        #result = process(i, caseData)
        result = solve(tiles, row, col)
        print >> out, 'Case #%s: %s' % (i,  result)
        print 'Case #%s: %s' % (i,  result)
    
    out.close()
