T = int(raw_input())

for case in xrange(1, T+1):
    items = raw_input().split()

    moves = [(items[i], int(items[i+1])) for i in xrange(1, int(items[0])*2+1, 2)]

    lastmove = {'O':0, 'B':0}
    currentpos = {'O':1, 'B':1}

    mintime = 0
    for move in moves:
        robot = move[0]
        dest = move[1]
        mintime = mintime + max(0, lastmove[robot]-mintime + abs(currentpos[robot]-dest))+1
        currentpos[robot] = dest
        lastmove[robot] = mintime
        #print move, currentpos, lastmove, mintime
    print "Case #%d: %d" %(case,mintime)

