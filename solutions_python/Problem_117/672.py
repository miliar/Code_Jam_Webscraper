#!/usr/bin/env python

import sys
import copy

def cut_pattern(n, m):
    pattern = []
    
    for i in range(m):
        block = []
        for j in range(n):
            row = [0] * m
            row[i] = 1
            block.append(row)
        pattern.append(block)
        
    for j in range(n):
        block = []
        for i in range(n):
            if(i == j):
                row = [1] * m
            else:
                row = [0] * m
            block.append(row)
        pattern.append(block)
        
    return pattern
        
#    for a in pattern:
#        for b in a:
#            print b
#        print ''

def cut_field(n, m, field, cut, height):
    fieldtmp = copy.deepcopy(field)
    for i in range(n):
        for j in range(m):
            if(cut[i][j] == 1):
                fieldtmp[i][j] = curheight
    return fieldtmp

def check_field(n, m, field, target, cut):
    for i in range(n):
        for j in range(m):
            if(cut[i][j] == 1):
                if(field[i][j] < target[i][j]):
                    return False
    return True

def match_field(n, m, field, target):
    for i in range(n):
        for j in range(m):
            if(field[i][j] != target[i][j]):
                return False
    return True

#c = cut_pattern(1,4)
#for a in c:
#    print a
#sys.exit()

f = open('/home/zinuzoid/Downloads/B-small-attempt0.in', 'r')
fout = open('/home/zinuzoid/Downloads/b.out', 'w')
cases =  int(f.readline())
for case in range(cases):
    raw = f.readline().split()
    n = int(raw[0])
    m = int(raw[1])
    print n,m
    
    target = []
    field = []
    minheight = 100
    maxheight = 0
    
    for i in range(n):
        row = f.readline().split()
        row = map(int, row)
        target.append(row)
        maxheight = max(row + [maxheight])
        minheight = min(row + [minheight])
    
    for a in target:
        print a
        
    for i in range(n):
        field.append([maxheight] * m)
        
    for a in field:
        print a
        
    
    print 'cut'
    curheight = maxheight - 1;
    for curheight in range(maxheight - 1, minheight - 1, -1):
        for c in cut_pattern(n, m):
            fieldtmp = cut_field(n, m, field, c, curheight)
            if(check_field(n, m, fieldtmp, target, c)):
                field = fieldtmp
                for a in fieldtmp:
                    print a
    
    matched = match_field(n, m, field, target)
    s = 'Case #' + str(case + 1) + ': ' + ('YES' if matched else 'NO')
    print s
    fout.write(s + '\n')
    #break
        
#    s = 'Case #' + str(case + 1) + ': ' + str(count)
#    print s
#    fout.write(s + '\n')
    
fout.close()
f.close()

# cut_pattern(10, 3)

