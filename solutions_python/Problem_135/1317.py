#! /usr/bin/env python
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as testdata:
        t = int(testdata.readline())
        for i in range(1, t+1):
            choice_1 = int(testdata.readline())
            for j in range(1, 5):
                if j == choice_1:
                    cards_1 = set([int(x) for x in testdata.readline().split()])
                else:
                    testdata.readline()
            choice_2 = int(testdata.readline())
            for j in range(1, 5):
                if j == choice_2:
                    cards_2 = set([int(x) for x in testdata.readline().split()])
                else:
                    testdata.readline()
            card_i = cards_1 & cards_2
            card_i_n = len(card_i)
            if card_i_n == 1:
                result = card_i.pop()
            elif card_i_n == 0:
                result = "Volunteer cheated!"
            else:
                result = "Bad magician!"
            print "Case #{}: {}".format(i, result)
