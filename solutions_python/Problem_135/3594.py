#!/usr/bin/env python

fptr = open('input.txt')

num_testcases = int(fptr.readline())

for case_num in range(num_testcases):
    guess1 = int(fptr.readline())
    # Board is [row #] [col #]
    board_matrix1 = []
    for j in range(4):
        board_matrix1.append(fptr.readline().split())

    guess2 = int(fptr.readline())
    # Board is [row #] [col #]
    board_matrix2 = []
    for j in range(4):
        board_matrix2.append(fptr.readline().split())
    
    possible_set = set(board_matrix1[guess1 - 1])

    chosen_cards = possible_set.intersection(board_matrix2[guess2 - 1])
    
    output_string = 'Case #' + str(case_num + 1) + ': '
    if len(chosen_cards) == 1:
        output_string += chosen_cards.pop()
    elif len(chosen_cards) == 0:
        # Volunteer Cheated
        output_string += 'Volunteer cheated!'
    elif len(chosen_cards) > 1:
        # Magician sucks
        output_string += 'Bad magician!'

    print output_string

