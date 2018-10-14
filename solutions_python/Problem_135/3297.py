data = open('A-small-attempt0.in')
num_tests = int(data.readline().strip())
for test in range(num_tests):
    line = data.readline().strip()
    row = int(line) - 1
    cards1 = []
    for i in range(4):
        line = data.readline().strip()
        cards1.append([int(c) for c in line.split()])
    row2 = int(data.readline().strip()) - 1
    cards2 = []
    for i in range(4):
        line = data.readline().strip()
        cards2.append([int(c) for c in line.split()])
    unique_card = 0
    is_unique = True
    for card in cards1[row]:
        if card in cards2[row2] and unique_card == 0:
           unique_card = card
        elif card in cards2[row2] and unique_card != 0:
            is_unique = False
    if unique_card == 0:
        print('Case #{0}: Volunteer cheated!'.format(test+1))
    elif is_unique == False:
        print('Case #{0}: Bad magician!'.format(test+1))
    else:
        print('Case #{0}: {1}'.format(test+1, unique_card))
