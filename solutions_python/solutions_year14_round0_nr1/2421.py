import sys

def get_row(input):
    index = int(input.readline())
    for i in range(1, 5):
        if i == index:
            row = [int(s) for s in input.readline().split(' ')]
        else:
            next(input)
    if not row:
        raise Exception("Invalid index for the selected row")
    return row

if __name__ == '__main__':
    with open('input/a') as input:
        for i in range(1, int(input.readline()) + 1):
            possible = get_row(input)
            possible2 = get_row(input)
            r = [x for x in possible2 if x in possible]
            if len(r) == 1:
                y = r[0]
            elif len(r) > 1:
                y = 'Bad magician!'
            else:
                y = 'Volunteer cheated!'
            print('Case #{:d}:'.format(i), y)


