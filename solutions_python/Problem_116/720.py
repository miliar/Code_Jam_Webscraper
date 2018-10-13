# Google Code Jam 2013 qualification round A.

import sys

lineSum = {}                  # Number of X's or O's in this line
# Each cell is in two or three lines: a row, a column, and maybe a diagonal.
linemap = [['r0','c0','d0'], ['r0','c1'], ['r0','c2'], ['r0','c3','d1'],
           ['r1','c0'], ['r1','c1','d0'], ['r1','c2','d1'], ['r1','c3'],
           ['r2','c0'], ['r2','c1','d1'], ['r2','c2','d0'], ['r2','c3'],
           ['r3','c0','d1'], ['r3','c1'], ['r3','c2'], ['r3','c3','d0']]
def init():
    global seenEmpty
    seenEmpty = False           # Haven't yet seen empty cell
    lines = [(line+str(num)) for line in 'rc' for num in range(4)]
    lines += ['d0', 'd1']
    for line in lines:
        for player in 'XO': lineSum[(line,player)] = 0

def add(line, player):
    if player == '.':
        global seenEmpty
        seenEmpty = True
        return
    if player == 'T':
        # A 'T' is like both an 'X' and an 'O'
        answer = add(line, 'X')
        if answer: return answer
        return add(line, 'O')
    lineSum[(line,player)] += 1
    if lineSum[(line,player)] == 4:
        return player + ' won'

def doCase(file):
    init()
    cells = ''
    for line in range(5):          # 5 to include trailing blank line
        cells += file.readline().strip()
    # cells is string of 'X', 'O', 'T', and '.' characters.
    for (lines, player) in zip(linemap, cells):
        for line in lines:
            answer = add(line, player)
            if answer: return answer
    if seenEmpty: return 'Game has not completed'
    return 'Draw'
    
def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        answer = doCase(file)
        print 'Case #{0}: {1}'.format(case, answer)
run()
