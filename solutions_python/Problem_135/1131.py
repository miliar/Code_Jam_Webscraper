from sys import stdin

for i in range(int(stdin.readline())):
    case = i + 1
    pos1 = int(stdin.readline())
    cards1 = [map(int, stdin.readline().split()) for x in range(4)]
    pos2 = int(stdin.readline())
    cards2 = [map(int, stdin.readline().split()) for x in range(4)]
    
    row1 = cards1[pos1 - 1]
    row2 = cards2[pos2 - 1]

    intersect_cards = list(set(row1) & set(row2))
    if len(intersect_cards) == 1:
        print "Case #{:}: {:}".format(case, intersect_cards[0])
    elif len(intersect_cards) == 0:
        print "Case #{:}: Volunteer cheated!".format(case)
    else:
        print "Case #{:}: Bad magician!".format(case)
