import sys

N = input()
row = [0, 0]
cards = [[[] for i in range(0, 4)] for i in [0, 1]]
for i in range(1, N + 1):
    for j in [0, 1]:
        row[j] = input() - 1
        for k in range(0, 4):
            cards[j][k] = raw_input().split(' ')
    inter = set(cards[0][row[0]]) & set(cards[1][row[1]])
    if len(inter) == 0:
        print 'Case #{0}: Volunteer cheated!'.format(i)
    elif len(inter) > 1:
        print 'Case #{0}: Bad magician!'.format(i)
    else:
        print 'Case #{0}: {1}'.format(i, min(inter))
