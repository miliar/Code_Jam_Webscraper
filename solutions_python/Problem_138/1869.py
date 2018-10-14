import random
from itertools import product
from pprint import pprint as pp
 
gridsize  = (6, 4)
minerange = (0.2, 0.6)
 
def gridandmines(gridsize=gridsize, minerange=minerange):
    xgrid, ygrid = gridsize
    minmines, maxmines = minerange
    minecount = xgrid * ygrid    
    minecount = random.randint(int(minecount*minmines), int(minecount*maxmines))
    grid = set(product(range(xgrid), range(ygrid)))
    mines = set(random.sample(grid, minecount))
    show = {xy:'.' for xy in grid}
    return grid, mines, show
 
def printgrid(show, gridsize=gridsize):
    xgrid, ygrid = gridsize
    grid = '\n'.join(''.join(show[(x,y)] for x in range(xgrid))
                     for y in range(ygrid))
    print( grid )
 
def resign(showgrid, mines, markedmines):
    for m in mines:
        showgrid[m] = 'Y' if m in markedmines else 'N'
 
def clear(x,y, showgrid, grid, mines, markedmines):
    if showgrid[(x, y)] == '.':
        xychar = str(sum(1
                         for xx in (x-1, x, x+1)
                         for yy in (y-1, y, y+1)
                         if (xx, yy) in mines ))
        if xychar == '0': xychar = '.'
        showgrid[(x,y)] = xychar
        for xx in (x-1, x, x+1):
            for yy in (y-1, y, y+1):
                xxyy = (xx, yy)
                if ( xxyy != (x, y)
                     and xxyy in grid
                     and xxyy not in mines | markedmines ):
                    clear(xx, yy, showgrid, grid, mines, markedmines)
 
if __name__ == '__main__':
    grid, mines, showgrid = gridandmines()
    markedmines = set([])
    print( __doc__ )
    print( '\nThere are %i true mines of fixed position in the grid\n' % len(mines) )
    printgrid(showgrid)
    while markedmines != mines:
        inp = raw_input('m x y/c x y/p/r: ').strip().split()
        if inp:
            if inp[0] == 'm':
                x, y = [int(i)-1 for i in inp[1:3]]
                if (x,y) in markedmines:
                    markedmines.remove((x,y))
                    showgrid[(x,y)] = '.'
                else:
                    markedmines.add((x,y))
                    showgrid[(x,y)] = '?'
            elif inp[0] == 'p':
                printgrid(showgrid)
            elif inp[0] == 'c':
                x, y = [int(i)-1 for i in inp[1:3]]
                if (x,y) in mines | markedmines:
                    print( '\nKLABOOM!! You hit a mine.\n' )
                    resign(showgrid, mines, markedmines)
                    printgrid(showgrid)
                    break
                clear(x,y, showgrid, grid, mines, markedmines)
                printgrid(showgrid)
            elif inp[0] == 'r':
                print( '\nResigning!\n' )
                resign(showgrid, mines, markedmines)
                printgrid(showgrid)
                break
 
    print( '\nYou got %i and missed %i of the %i mines'
           % (len(mines.intersection(markedmines)),
              len(markedmines.difference(mines)),
              len(mines)) )
