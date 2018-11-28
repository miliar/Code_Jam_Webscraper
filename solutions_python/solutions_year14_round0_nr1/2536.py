T = int(input())

def readBoard():
    board = []
    for r in range(4):
        board.append(map(int, input().strip().split()))
    return board

for test in range(T):
    ans1 = int(input())
    board1 = readBoard()
    ans2 = int(input())
    board2 = readBoard()

    intsec = set(board1[ans1-1]).intersection(set(board2[ans2-1]))
    if len(intsec) == 1:
        out = str(intsec.pop())
    elif not intsec:
        out = 'Volunteer cheated!'
    else:
        out = 'Bad magician!'

    print('Case #{}: {}'.format(test+1, out))

