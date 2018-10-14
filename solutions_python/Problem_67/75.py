#!/usr/local/bin/python

import sys

def proc_case():
    R = int(raw_input())
    cells = set()
    cellsnext =set()
    result = 0

    for i in range(R):
        x1,y1,x2,y2 = map(int, (raw_input()).split())
        for j in range(x1,x2+1):
            for k in range(y1,y2+1):
                cells.add((j,k))
    
    while len(cells):
        for cell in cells:
            if (cell[0],cell[1]-1) in cells or (cell[0]-1,cell[1]) in cells:
                cellsnext.add(cell)
            if (cell[0],cell[1]+1) not in cells:
                if (cell[0]-1,cell[1]+1) in cells:
                    cellsnext.add((cell[0],cell[1]+1))
        cells.clear()
        cells = set(cellsnext)
        cellsnext.clear()
        result+=1

    return result

def proc_all():
    n_case=int(sys.stdin.readline().rstrip())
    for i in range(n_case):
        print 'Case #%d: %d'%(i+1,proc_case())

proc_all()
