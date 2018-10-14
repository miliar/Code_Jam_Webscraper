dirs = [
[ [0,0], [0,1], [0,2], [0,3], ],
[ [1,0], [1,1], [1,2], [1,3], ],
[ [2,0], [2,1], [2,2], [2,3], ],
[ [3,0], [3,1], [3,2], [3,3], ],
[ [0,0], [1,0], [2,0], [3,0], ],
[ [0,1], [1,1], [2,1], [3,1], ],
[ [0,2], [1,2], [2,2], [3,2], ],
[ [0,3], [1,3], [2,3], [3,3], ],
[ [0,0], [1,1], [2,2], [3,3], ],
[ [0,3], [1,2], [2,1], [3,0], ]
]

for TC in range(1, input()+1):
    grid = []
    for i in range(4):
        grid += [raw_input()]
    for dir in dirs:
        win = 0
        line = [grid[c[0]][c[1]] for c in dir]
        x = 'X' in line
        o = 'O' in line
        if '.' in line:
            continue
        if x and o:
            continue
        if x:
            win = 1
            break
        else:
            win = 2
            break
    if win == 0 and '.' in line:
        print 'Case #%d: Game has not completed' % TC
    elif win == 0:
        print 'Case #%d: Draw' % TC
    elif win == 1:
        print 'Case #%d: X won' % TC
    elif win == 2:
        print 'Case #%d: O won' % TC
    raw_input()