def main():
    with open('input.txt') as f:
        data = f.read()
    lines = data.split('\n')[1:]
    boards = []
    for i, l in enumerate(lines):
        if i % 5 == 0:
            boards.append([])
        if i % 5 != 4:
            boards[len(boards) - 1].append(list(l))
    boards.pop()

    for i, b in enumerate(boards):
        result = checkboard(b)
        if result == 0:
            print('Case #{0}: {1}'.format(i + 1, 'Game has not completed'))
        elif result == 1:
            print('Case #{0}: {1}'.format(i + 1, 'Draw'))
        elif result == 2:
            print('Case #{0}: {1}'.format(i + 1, 'X won'))
        elif result == 3:
            print('Case #{0}: {1}'.format(i + 1, 'O won'))

def checkboard(board):
    # Horizontal
    for row in board:
        if all(c in 'XT' for c in row):
            return 2
        if all(c in 'OT' for c in row):
            return 3

    # Vertical
    for i in range(4):
        col = list(r[i] for r in board)
        if all(c in 'XT' for c in list(col)):
            return 2
        if all(c in 'OT' for c in list(col)):
            return 3

    # Diagonal
    if board[0][0] in 'XT' and board[1][1] in 'XT' and board[2][2] in 'XT' and board[3][3] in 'XT':
        return 2
    if board[0][0] in 'OT' and board[1][1] in 'OT' and board[2][2] in 'OT' and board[3][3] in 'OT':
        return 3

    if board[0][3] in 'XT' and board[1][2] in 'XT' and board[2][1] in 'XT' and board[3][0] in 'XT':
        return 2
    if board[0][3] in 'OT' and board[1][2] in 'OT' and board[2][1] in 'OT' and board[3][0] in 'OT':
        return 3

    # Not completed
    for row in board:
        if any(c == '.' for c in row):
            return 0

    # Draw
    return 1

if __name__ == '__main__':
    main()

