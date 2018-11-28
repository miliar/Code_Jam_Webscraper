import math
import sys

infile = open('test.in', 'r')
cases = int(infile.readline().strip())

for case in range(cases):
    cur = { 'O': 1, 'B': 1 }
    prevSum = 0
    prevCol = ''
    moves = infile.readline().strip().split()

    totalTime = int(0)
    it = iter(moves)

    numMoves = int(next(it))
    
    for move in range(numMoves):
        color = next(it)
        button = int(next(it))
        if color == prevCol:
            time = int(math.fabs(cur[color] - button) + 1)
            prevSum = prevSum + time
            totalTime = totalTime + time
            prevCol = color
            cur[color] = button
        else:
            time = int(max(math.fabs(cur[color] - button) - prevSum, 0) + 1)
            prevSum = time
            totalTime = totalTime + time
            prevCol = color
            cur[color] = button

    print "Case #{0}: {1}".format(case+1, totalTime)
