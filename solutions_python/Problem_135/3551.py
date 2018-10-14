__author__ = 'PC'

fin = open('A-small-attempt1.in', 'r')
fout = open('A-small-attempt1.out', 'w')

t = int(fin.readline())
for case_number in range(t):
    a_1 = int(fin.readline())
    board = [list(map(int, fin.readline().split())) for i in range(4)]
    var_1 = set(board[a_1 - 1])

    a_2 = int(fin.readline())
    board = [list(map(int, fin.readline().split())) for i in range(4)]
    var_2 = set(board[a_2 - 1])

    cross = var_1.intersection(var_2)
    if len(cross) == 1:
        print('Case #%d: %d' % (case_number + 1, cross.pop()), file = fout)
    elif len(cross) > 1:
        print('Case #%d: Bad magician!' % (case_number + 1), file = fout)
    else:
        print('Case #%d: Volunteer cheated!' % (case_number + 1), file = fout)