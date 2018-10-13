#! /usr/bin/python

import sys

# Return a set representing the cards
# in the specified row. Row is indexed by 1
def read_row_cards(fh, row):
    row_set = set()
    for i in range(1, 5):
        row_cards = f.readline().split()
        if i == row:
            row_set = set(row_cards)
    return row_set

#
# Main
#
if len(sys.argv) != 2:
    print 'Incorrect arguments'
    sys.exit(0)

f = open(sys.argv[1])

# Read number of test cases from the file
n_tests = int(f.readline())

for i in range(1, n_tests+1):

    # Read the initial row containing the chosen card
    initial_row = int(f.readline())

    # Read the cards in intial row into a set
    initial_cards = read_row_cards(f, initial_row)

    # Read the row after shuffling
    next_row = int(f.readline())
    next_cards = read_row_cards(f, next_row)

    # Intersect to find the possible solution
    solutions = initial_cards.intersection(next_cards)

    output = ""
    if len(solutions) == 1:
        output = str(solutions.pop())
    elif len(solutions) == 0:
        output = "Volunteer cheated!"
    else:
        output = "Bad magician!"
    print 'Case #{}: {}'.format(i, output)
