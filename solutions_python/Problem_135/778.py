from sys import stdin

input_it = iter(stdin)

T = int(input_it.next())

for t in range(T):

    # interpret input
    choice1 = int(input_it.next())
    for i in range(4):
        line = input_it.next()
        if i + 1 == choice1:
            cards1 = list(int(card) for card in line.split())

    choice2 = int(input_it.next())
    for i in range(4):
        line = input_it.next()
        if i + 1 == choice2:
            cards2 = list(int(card) for card in line.split())

    cards = [card for card in cards1 if card in cards2]

    if len(cards) == 1:
        y = cards[0]
    elif len(cards) == 0:
        y = 'Volunteer cheated!'
    else:
        y = 'Bad magician!'

    print 'Case #{t}: {y}'.format(t=t+1, y=y)
