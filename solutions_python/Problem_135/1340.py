import sys

num_tricks = int(sys.stdin.readline())

for i in range(0,num_tricks):
    first_row_num = int(sys.stdin.readline())
    rows = [sys.stdin.readline() for _ in range(0,4)]
    first_row = rows[first_row_num - 1]
    first_row_set = set(map(int, first_row.split(' ')))
    second_row_num = int(sys.stdin.readline())
    rows = [sys.stdin.readline() for _ in range(0,4)]
    second_row = rows[second_row_num - 1]
    second_row_set = set(map(int, second_row.split(' ')))

    cards = first_row_set & second_row_set

    if len(cards) == 0:
        result = 'Volunteer cheated!'
    elif len(cards) == 1:
        result = list(cards)[0]
    else:
        result = 'Bad magician!'

    print('Case #{0}: {1}'.format(i + 1, result))
