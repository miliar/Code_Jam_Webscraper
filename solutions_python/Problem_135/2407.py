import sys

for i in range(input()):
    first_ans = input()
    for j in range(4):
        row = raw_input()
        if first_ans == j+1:
            first_row = map(int, row.split())
    second_ans = input()
    for j in range(4):
        row = raw_input()
        if second_ans == j+1:
            second_row = map(int, row.split())
    card = list(set(first_row) & set(second_row))
    sys.stdout.write('Case #%d: ' % (i+1))
    if len(card) == 1:
        print card[0]
    elif len(card) > 1:
        print 'Bad magician!'
    else:
        print 'Volunteer cheated!'




