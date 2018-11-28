# Code Jam 2014 - Qualification Round
# Problem A: Magic Trick
# chamrtom


def loadcards(row):
    result = None
    for i in range(1, 4+1):
        cards = set(raw_input().split())
        if i == row:
            result = cards
    return result


T = int(raw_input())

for t in range(1, T+1):
    row1 = int(raw_input())
    set1 = loadcards(row1)
    row2 = int(raw_input())
    set2 = loadcards(row2)
    intersection = set1.intersection(set2)

    if len(intersection) == 1:
        print "Case #{0}: {1}".format(t, intersection.pop())
    elif len(intersection) == 0:
        print "Case #{0}: Volunteer cheated!".format(t)
    else:
        print "Case #{0}: Bad magician!".format(t)
