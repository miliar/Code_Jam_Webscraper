check_number = [[0,1,2,3],
                [4,5,6,7],
                [8,9,10,11],
                [12,13,14,15],
                [0,4,8,12],
                [1,5,9,13],
                [2,6,10,14],
                [3,7,11,15],
                [0,5,10,15],
                [3,6,9,12]]
xwin = 'X won'
owin = 'O won'
draw = 'Draw'
go = 'Game has not completed'

def check(number):
    w = [board[x] for x in number]
    if '.' in w:
        return 'Draw'
    if 'O' in w and 'X' in w:
        return 'Draw'
    if 'O' in w:
        return 'O'
    else:
        return 'X'

in_data = open('A-large.in').readlines()
in_data = [x.strip() for x in in_data]
T = int(in_data[0])
in_data = in_data[1:]
res = open('result', 'w')

for i in range(T):
    board_str = ''.join(in_data[0:4])
    board = list(board_str)
    in_data = in_data[5:]
    for num in check_number:
        r = check(num)
        if r=='X' or r=='O':
            break
    if r=='X':
        output = 'Case #' + str(i+1) + ': ' + xwin + '\n'
        res.write(output)
        continue
    if r=='O':
        output = 'Case #' + str(i+1) + ': ' + owin + '\n'
        res.write(output)
        continue
    if '.' in board:
        output = 'Case #' + str(i+1) + ': ' + go + '\n'
    else:
        output = 'Case #' + str(i+1) + ': ' + draw + '\n'
    res.write(output)