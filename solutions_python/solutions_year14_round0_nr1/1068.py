def solve(row1, cards1, row2, cards2):
    """ solve the problem """

    constraint1 = set( cards1[row1] )
    constraint2 = set( cards2[row2] )

    answers = constraint1.intersection(constraint2)

    if len(answers) == 1:
        return answers.pop()
    elif len(answers) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'


def parse():
    """ parse input """

    row1 = int(input()) - 1
    cards1 = []
    for i in range(4):
        cards1.append([int(i) for i in input().split()])

    row2 = int(input()) - 1
    cards2 = []
    for i in range(4):
        cards2.append([int(i) for i in input().split()])

    return row1, cards1, row2, cards2


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
