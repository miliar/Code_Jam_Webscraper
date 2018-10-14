def strtoboard(board):
    return [row.split(' ') for row in board.splitlines()]

numcases = int(input())
for numcase in range(numcases):
    ans1 = int(input())
    board1 = strtoboard('\n'.join([input() for i in range(4)]))
    ans2 = int(input())
    board2 = strtoboard('\n'.join([input() for i in range(4)]))

    pos = set(board1[ans1 - 1]) & set(board2[ans2 - 1])

    if len(pos) is 1:
        ans = list(pos)[0]
    elif len(pos) > 1:
        ans = 'Bad magician!'
    else:
        ans = 'Volunteer cheated!'
    

    print('Case #%s: %s' % (numcase + 1, ans))
