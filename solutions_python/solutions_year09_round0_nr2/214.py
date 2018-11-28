'''
Jirasak Chirathivat
'''

import os
import os.path
import sys
sys.setrecursionlimit(1000000000)

#### CHANGE HERE ####
filename = 'b.txt'
#### CHANGE HERE ####

def spread(matrix, i, j):
    north, west, east, south = (None, None, None, None)
    checks = []
    value = matrix[i][j]
    if i > 0:
        north = matrix[i - 1][j]
        if north < value:
            checks.append(north)
    if i < len(matrix) - 1:
        south = matrix[i + 1][j]
        if south < value:
            checks.append(south)
    if j > 0:
        west = matrix[i][j - 1]
        if west < value:
            checks.append(west)
    if j < len(matrix[0]) - 1:
        east = matrix[i][j + 1]
        if east < value:
            checks.append(east)
    
    if len(checks) == 0:
        return None
    
    mincheck = min(checks)
    if mincheck == north:
        return i - 1, j
    if mincheck == west:
        return i, j - 1
    if mincheck == east:
        return i, j + 1
    if mincheck == south:
        return i + 1, j

def change(area, oldchar, newchar):
    maxi = len(area)
    maxj = len(area[0])
    
    for row in range(maxi):
        for col in range(maxj):
            if area[row][col] == oldchar:
                area[row][col] = newchar

def calibrate(area):
    maxi = len(area)
    maxj = len(area[0])
    
    startnum = 97
    for row in range(maxi):
        for col in range(maxj):
            value = area[row][col]
            if type(value) == type(0):
                change(area, value, chr(startnum))
                startnum += 1

def process(casenum, casedata):
    #### CHANGE HERE ####
    matrix = casedata[0]
    
    maxi = len(matrix)
    maxj = len(matrix[0])
    
    area = []
    for row in range(maxi):
        newrow = []
        for col in range(maxj):
            newrow.append(None)
        area.append(newrow)
    
    startNum = 0
    for i in range(maxi):        
        for j in range(maxj):
            result = spread(matrix, i, j)
            
            # If it cannot spread
            if result == None:
                if area[i][j] == None: # If it has no value, assign!
                    startNum += 1
                    currchar = startNum
                    area[i][j] = currchar
                    continue
                else:
                    continue
            
            # If it can spread        
            si, sj = result
            if area[i][j] != None:
                currchar = area[i][j]
            else:
                startNum += 1
                currchar = startNum
                area[i][j] = currchar
            
            if area[si][sj] != None:
                anotherchar = area[si][sj]
                change(area, currchar, anotherchar)
                #area[i][j] = anotherchar
                # set all the 
            else:
                area[si][sj] = currchar
    
    calibrate(area)
    lines = [' '.join(x) for x in area]
    lines = '\n'.join(lines)
    
    return '\n' + lines
    #### CHANGE HERE ####

if __name__ == '__main__':
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('bout.txt', 'w')
    casefile = file('casefile.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    # special 
    
    line = 1
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        dimension = aread[line].split(' ')
        dimrow, dimcol = (int(dimension[0]), int(dimension[1]))
        matrix = []
        for erow in aread[line + 1:dimrow + line + 1]:
            rows = erow.split(' ')
            rows = [int(x) for x in rows]
            matrix.append(rows)
        #### CHANGE HERE ####
        
        #### CHANGE HERE ####
        caseData = (matrix,)
        tomove = 1 + dimrow
        #### CHANGE HERE ####

        if False:
            print >> casefile, 'Case #%s' % i
            print >> casefile, '%s\n' % '\n'.join(aread[line: line + tomove])
            print >> casefile, '%s\n\n\n' % ('\n'.join([str(x) for x in caseData]))
        
        #### CHANGE HERE ####
        line += tomove
        #### CHANGE HERE
        
        print >> out, 'Case #%s: %s' % (i,  process(i, caseData))
    
    casefile.close()
    out.close()
    #os.startfile('out.txt')
    #os.startfile('casefile.txt')  
