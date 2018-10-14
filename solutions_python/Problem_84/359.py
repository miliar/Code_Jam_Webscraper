#!/usr/bin/python
import sys
from copy import deepcopy

def chmat(x, y, mat, r, c):
    #print x, y, r, c
    if mat[y][x] == '#':
        if x+1 < c and y+1 < r:
            if mat[y][x] == '#' and mat[y][x+1] == '#' and mat[y+1][x] == '#' and mat[y+1][x+1] == '#':
                return 0
            elif mat[y][x] == '#' or mat[y][x+1] == '#' or mat[y+1][x] == '#' or mat[y+1][x+1] == '#':
                return 1
            else:
                return 2
        elif x+1<c:
            if mat[y][x] == '#' or mat[y][x+1] == '#':
                return 1
            else:
                return 2
        elif y+1<r:
            if mat[y][x] == '#' or mat[y+1][x] == '#':
                return 1
            else:
                return 2
        else:
            if mat[y][x] == '#':
                return 1
            else:
                return 2
    else:
        return 2
        

if len(sys.argv) == 3:
    lines = open(sys.argv[1], 'r').readlines()
    fw = open(sys.argv[2], 'w')
else:
    sys.exit('Usage: %s in_filename out_filename' % sys.argv[0])


"""
lines = ['3'
,'2 3'
,'###'
,'###'
,'1 1'
,'.'
,'4 5'
,'.##..'
,'.####'
,'.####'
,'.##..']
"""

numofcases = int(lines[0])
cursor = 1
for i in range(0, numofcases):
    
    param = lines[cursor].replace('\n', '').split(' ')
    cursor += 1
    
    R = int(param[0])
    C = int(param[1])
    
    mat = []
    for j in range(0, R):
        mat.append(list(lines[cursor].replace('\n', '')))
        cursor += 1
    print mat
    
    result = ''
    mat_out = deepcopy(mat)
    for j in range(0, R):
        for k in range(0, C):
            if mat[j][k] != '0':
                ch = chmat(k, j, mat, R, C)
                if ch == 0:
                    mat_out[j][k] = '/'
                    mat_out[j+1][k+1] = '/'
                    mat_out[j][k+1] = "\\"
                    mat_out[j+1][k] = "\\"
                    mat[j][k] = '0'
                    mat[j][k+1] = '0'
                    mat[j+1][k] = '0'
                    mat[j+1][k+1] = '0'
                elif ch == 1:
                    result = 'Impossible'
                    break
        if result != '':
            break
    
    
    print 'Case #%d:' % (i+1)
    fw.write('Case #%d:\n' % (i+1))
    
    if result == '':
        for j in range(0, R):
            print ''.join(mat_out[j])
            fw.write(''.join(mat_out[j]) + '\n')
    else:
        print result
        fw.write(result + '\n')
    
fw.close()
