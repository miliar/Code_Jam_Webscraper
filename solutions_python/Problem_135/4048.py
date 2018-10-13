import sys

def get_card(boards, choices):
    row1 = boards[0][choices[0] - 1]
    row2 = boards[1][choices[1] - 1]
    intersect = filter(lambda x: x in row1, row2)
    if len(intersect) == 1:
        return intersect[0]
    elif len(intersect) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'

if __name__ == '__main__':
    inp = sys.stdin
    count = int(inp.readline())
    for i in range(count):
        boards = [[], []]
        choices = []
        for board in boards:
            choices.append(int(inp.readline()))
            for j in range(4):
                board_row = inp.readline().strip().split(' ')
                board.append((int(board_row[0]), int(board_row[1]),
                              int(board_row[2]), int(board_row[3])))
        print 'Case #%d:' % (i + 1), get_card(boards, choices)

