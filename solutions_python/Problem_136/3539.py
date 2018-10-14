'''
Created on Apr 1, 2013

@author: pawel
'''
import sys

def read_line(file):
    return file.readline().strip('\n').split(' ')

def read_cards_info(file):
    cards = [[None for x in range(4)] for x in range(4)]
    for i in range(4):
        raw_line2 = read_line(file)
        for j, card in enumerate(raw_line2):
            cards[i][j] = card
    return cards;

def read_case_info(file):
    data = {}
    data['first_answer'] = int(read_line(file)[0]) - 1
    data['first_cards'] = read_cards_info(file)
    data['second_answer'] = int(read_line(file)[0]) - 1
    data['second_cards'] = read_cards_info(file)
    return data


def get_possible_cards(row_number, cards):
    return cards[row_number];


def solve_case(data):
    first_possible_cards = get_possible_cards(data['first_answer'], data['first_cards'])
    second_possible_cards = get_possible_cards(data['second_answer'], data['second_cards'])
    possible_cards = set(first_possible_cards).intersection(set(second_possible_cards));
    number_of_possible_cards = len(possible_cards)
    if  number_of_possible_cards == 1:
        return list(possible_cards)[0]
    elif number_of_possible_cards > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

file = open(sys.argv[1], 'r')
number_of_cases = int(file.readline().strip())
counter = 0
results = []
while number_of_cases > counter:
    case_info = read_case_info(file)
    results.append(str(solve_case(case_info)))
    counter += 1

file_output = open(sys.argv[2], 'w')
for index, result in enumerate(results):
    file_output.write('Case #' + str(index + 1) +  ': ' + result + '\n')
