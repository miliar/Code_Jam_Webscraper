from sys import stdout

first_choice = 0
second_choice = 0


def solve(first_cards, second_cards, first_choice, second_choice):
    first_row = first_cards[first_choice - 1]
    second_row = second_cards[second_choice - 1]

    solutions = []

    for card in first_row:
        if card in second_row:
            solutions.append(card)

    if len(solutions) == 0:
        print "Volunteer cheated!"
    elif len(solutions) == 1:
        print solutions[0]
    else:  # More than one solution
        print "Bad magician!"

num_cases = int(raw_input())

for case in range(1, num_cases + 1):

    first_choice = int(raw_input())

    first_cards = [raw_input() for x in range(4)]
    first_cards = map(lambda x: x.split(' '), first_cards)

    second_choice = int(raw_input())

    second_cards = [raw_input() for x in range(4)]
    second_cards = map(lambda x: x.split(' '), second_cards)

    stdout.write("Case #%i: " % (case))
    solve(first_cards, second_cards, first_choice, second_choice)
