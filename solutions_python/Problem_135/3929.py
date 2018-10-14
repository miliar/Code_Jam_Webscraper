import sys

lines = open('A-small-attempt1.in').readlines()
#lines = open('test.txt').readlines()
num_games = int(lines[0])

i = 1
ig = 0
while ig < num_games:
    before_row = int(lines[i])
    i = i + 1
    board = []
    ib = i
    while i < ib + 4:
        board.append(map(int, lines[i].split()))
        i = i + 1
    after_row = int(lines[i])
    i = i + 1
    board_next = []
    ib = i
    while i < ib + 4:
        board_next.append(map(int, lines[i].split()))
        i = i + 1
    ig = ig + 1

    poss = set(board[before_row - 1]) & set(board_next[after_row - 1])
    if len(poss) == 1:
        print 'Case #%d: %d' % (ig, [j for j in poss][0])
    elif len(poss) > 0:
        print 'Case #%d: Bad magician!' % ig
    else:
        print 'Case #%d: Volunteer cheated!' % ig
