from sys import argv

import linecache

def result(cards):
    if len(cards) == 1:
        r = cards.pop()
    elif len(cards) == 0:
        r = 'Volunteer cheated!'
    else:
        r = 'Bad magician!'

    return r


filename = argv[1]
num = int(linecache.getline(filename, 1))

for i in range(num):
    turn_one_index = 2 + i*10
    turn_two_index = 7 + i*10

    # First and second row for turns.
    turn_one_row = int(linecache.getline(filename, turn_one_index))
    turn_two_row = int(linecache.getline(filename, turn_two_index))

    # Get cards in first row configuration.
    cards_one = set(linecache.getline(filename,
        turn_one_index+turn_one_row).split())
    cards_two = set(linecache.getline(filename,
        turn_two_index+turn_two_row).split())

    print "Case #%i: %s" % ((i+1), result(cards_one.intersection(cards_two)))

