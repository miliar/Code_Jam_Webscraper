#!/usr/bin/env python

#PEGMAN!

TEST="""4
2 1
^
^
2 2
>v
^<
3 3
...
.^.
...
1 1
."""
#raw_input = iter(TEST.splitlines()).next
#raw_input = iter(open("A-small-attempt1.in", 'r').readlines()).next

def p(GRID):
    for p in GRID:
        print p

def find_arrow(ix,jx,cell,R,C,GRID):
    if cell == '^':
        d = (-1, 0)
    elif cell == '>':
        d = (0, 1)
    elif cell == '<':
        d = (0, -1)
    elif cell == 'v':
        d = (1, 0)
    
    i, j = ix+d[0], jx+d[1]
    while (0<=i and i<R) and (0<=j and j<C):
        if GRID[i][j] != ".":
            return True
        i, j = i+d[0], j+d[1]
    return False

def solve(R,C, GRID):
    assert(len(GRID[0]) == C)
    assert(len(GRID) == R)

    connected_arrows = set()
    killer_arrows = set()

    for ix, row in enumerate(GRID):
        for jx, cell in enumerate(row):
            if cell == '.':
                continue
            elif find_arrow(ix,jx,cell,R,C,GRID):
                # this arrow connects to another. not a killer
                connected_arrows.add( (ix,jx) )
            else:
                # doesn't connect. killer arrow!
                killer_arrows.add( (ix, jx) )

    # could every killer arrow be connected?
    rotate = 0
    for killer in killer_arrows:
        if (find_arrow(killer[0], killer[1], '<', R, C, GRID) or
            find_arrow(killer[0], killer[1], '>', R, C, GRID) or
            find_arrow(killer[0], killer[1], '^', R, C, GRID) or
            find_arrow(killer[0], killer[1], 'v', R, C, GRID)):
            # can rotate. must rotate.
            rotate += 1
        else:
            #p(GRID)
            #print rotate
            #import pdb;pdb.set_trace()
            return "IMPOSSIBLE"

    #p(GRID)
    #print rotate
    #import pdb;pdb.set_trace()
    return rotate

T = int(raw_input())
for case in range(1,T+1):
    R,C = map(int, raw_input().strip().split())
    grid = [raw_input().strip() for i in range(R)]
    print("Case #%s: %s" % (case, solve(R, C, grid)))
