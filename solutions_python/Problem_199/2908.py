t = int(raw_input())
for i in xrange(1, t+1):
    board, flipper_size = raw_input().split()
    flipper_size = int(flipper_size)
    griddle = []
    count = 0
    for char in board:
        if char == '-':
            griddle.append(0)
        else:
            griddle.append(1)
    for j in xrange(len(board) - flipper_size + 1):
        if griddle[j] % 2 == 0:
            for k in xrange(j, j+flipper_size):
                griddle[k] += 1
                griddle[k] %= 2
            count += 1
    if all(griddle[-flipper_size] == x for x in griddle[-flipper_size:]):
        print "Case #%d: %d" % (i,count)
    else:
        print "Case #%d: IMPOSSIBLE" % i