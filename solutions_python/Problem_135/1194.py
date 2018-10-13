
def cards_in_row(cards, row):
    return set(cards[row-1])

def response(begin, row, end, row2):
    first = cards_in_row(begin, row)
    last = cards_in_row(end, row2)
    
    ints = first.intersection(last)
    if len(ints) == 0:
        return 'Volunteer cheated!'
    elif len(ints) > 1:
        return 'Bad magician!'
    else:
        return list(ints)[0]

def read_board():
    lines = []
    for i in range(4):
        lines.append(raw_input().split(' '))
    return lines
if __name__ == '__main__':
    T = int(raw_input())
    for i in range(T):
        r1 = int(raw_input())
        b1 = read_board()
        r2 = int(raw_input())
        b2 = read_board()

        print('Case #%d: %s' % (i + 1, response(b1, r1, b2, r2)))
