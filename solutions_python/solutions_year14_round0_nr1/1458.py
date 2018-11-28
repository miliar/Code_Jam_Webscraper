__author__ = 'cheungkt'

import sys


def main():
    with open(sys.argv[1], 'r') as test:
        for i in range(1, int(test.readline()) + 1):
            initial_row = int(test.readline())
            initial_cards = []
            for j in range(1, 5):
                if j == initial_row:
                    temp = test.readline().split()
                    initial_cards = [int(x) for x in temp]
                else:
                    test.readline()
            new_row = int(test.readline())
            new_cards = []
            for k in range(1, 5):
                if k == new_row:
                    temp = test.readline().split()
                    new_cards = [int(x) for x in temp]
                else:
                    test.readline()
            result, card = checkforcard(initial_cards, new_cards)
            if result == 0:
                print 'Case #' + str(i) + ': Volunteer cheated!'
            elif result > 1:
                print 'Case #' + str(i) + ': Bad magician!'
            else:
                print 'Case #' + str(i) + ': ' + str(card)


def checkforcard(original, new):
    count = 0
    card = 0
    for i in original:
        if i in new:
            count += 1
            card = i
    return count, card


if __name__ == '__main__':
    main()