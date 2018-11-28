'''
Problem A. Magic Tricks
'''

t = int(raw_input())
for _ in range(1, t+1):
    row1 = int(raw_input())
    cards1 = [map(int, raw_input().split()) for i in range(4)]
    row2 = int(raw_input())
    cards2 = [map(int, raw_input().split()) for i in range(4)]
    result = list(set(cards1[row1-1]).intersection(set(cards2[row2-1])))
    if len(result) == 1:
        print 'Case #' + str(_) + ': ' + str(result[0])
    elif len(result) > 1:
        print 'Case #' + str(_) + ': Bad magician!'
    else:
        print 'Case #' + str(_) + ': Volunteer cheated!'