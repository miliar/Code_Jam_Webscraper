#!/usr/bin/python

import sys

# Check if a lawn configuration is possible
def validate_lawn(lawn):
    row_max = [max(row) for row in lawn]
    col_max = [max([row[x] for row in lawn]) for x in range(len(lawn[0]))]

    # Impossible if the height at any point is less than the max
    # height on both its row and its column    
    for r in range(len(lawn)):
        for c in range(len(lawn[r])):
            height = lawn[r][c]
            if height < row_max[r] and height < col_max[c]:
                return False

    return True

with open(sys.argv[1], 'r') as infile:
    cases = int(infile.readline().strip())

    for n in range(cases):
        print 'Case #' + str(n+1) + ': ',
        size = infile.readline().split()
        rows = int(size[0])

        lawn = []
        for x in range(rows):
            cells = infile.readline().split()
            lawn += [[int(x) for x in cells]]
       
        if validate_lawn(lawn):
            print 'YES'
        else:
            print 'NO'
