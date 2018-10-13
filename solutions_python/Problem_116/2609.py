wins = [[0, 4, 8, 12],
        [1, 5, 9, 13],
        [2, 6, 10, 14],
        [3, 7, 11, 15],
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15],
        [0, 5, 10, 15],
        [3, 6, 9, 12]]

myfile = open('A-large.in')

for case in range(int(myfile.readline())):
    board = ''
    board += myfile.readline().strip()
    board += myfile.readline().strip()
    board += myfile.readline().strip()
    board += myfile.readline().strip()

    winner = ''
    completed = True

    for win in wins:
        line = ''

        for num in win:
            line += board[num]

        if line.count('.') > 0:
            completed = False

        if line.replace('T', 'X') == 'XXXX':
            winner = 'X'
            break
        elif line.replace('T', 'O') == 'OOOO':
            winner = 'O'
            break

    if winner == '' and not completed:
        print('Case #%d: Game has not completed' % (case+1))
    else:
        if winner == '':
            print('Case #%d: Draw' % (case+1))
        elif winner == 'X':
            print('Case #%d: X won' % (case+1))
        elif winner == 'O':
            print('Case #%d: O won' % (case+1))

    myfile.readline()
