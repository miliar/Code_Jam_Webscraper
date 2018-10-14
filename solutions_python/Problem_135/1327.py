num_tests = int(raw_input())

for t in range(num_tests):
    
    case = t + 1
    num_row_first = int(raw_input())
    
    cards_1 = matrix = [[0 for i in range(4)] for j in range(4)]
    cards_2 = matrix = [[0 for i in range(4)] for j in range(4)]
    
    for i in range(4):
        line = raw_input()
        cards = line.split(' ')
        for j in range(4):
            cards_1[i][j] = cards[j]

    num_row_second = int(raw_input())
    for i in range(4):
        line = raw_input()
        cards = line.split(' ')
        for j in range(4):
            cards_2[i][j] = cards[j]

    row_first = cards_1[num_row_first - 1]
    row_second = cards_2[num_row_second - 1]

    num_pos = 0
    for card_1 in row_first:
        for card_2 in row_second:
            
            if (card_1 == card_2):
                num_pos += 1
                chosen_pos = card_1

    if (num_pos == 0):
        ans = 'Volunteer cheated!'
    elif (num_pos > 1):
        ans = 'Bad magician!'
    else:
        ans = chosen_pos

    print 'Case #' + str(case) +  ': ' +  str(ans)




