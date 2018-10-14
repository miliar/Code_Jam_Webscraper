def test(grid):
    for i in xrange(4):
        if all([x in "TX" for x in grid[i]]) or \
           all([grid[j][i] in "TX" for j in xrange(4)]):
            return 'X'
        if all([x in "TO" for x in grid[i]]) or \
           all([grid[j][i] in "TO" for j in xrange(4)]):
            return 'O'
    if all([grid[i][i] in "TX" for i in xrange(4)]) or \
       all([grid[3-i][i] in "TX" for i in xrange(4)]):
        return 'X'
    if all([grid[i][i] in "TO" for i in xrange(4)]) or \
       all([grid[3-i][i] in "TO" for i in xrange(4)]):
        return 'O'
    if "." in "".join(grid):
        return 'N'
    return 'D'

T = input()
for case in xrange(T):
    grid = []
    for i in xrange(4):
        grid.append(raw_input().strip())
    raw_input()
    
    r = test(grid)
    if r == 'X':
        print "Case #%d: X won" % (case + 1)
    elif r == 'O':
        print "Case #%d: O won" % (case + 1)
    elif r == 'D':
        print "Case #%d: Draw" % (case + 1)
    else:
        print "Case #%d: Game has not completed" % (case + 1)