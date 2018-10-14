import sys
input = open("A-small-attempt2.in").read()
input = input.split("\n")

cases = input.pop(0)

for i in range(int(cases)):
    row1 = int(input.pop(0))
    cards1 = {}
    cards1[1] = set(input.pop(0).split())
    cards1[2] = set(input.pop(0).split())
    cards1[3] = set(input.pop(0).split())
    cards1[4] = set(input.pop(0).split())
    row2 = int(input.pop(0))
    cards2 = {}
    cards2[1] = set(input.pop(0).split())
    cards2[2] = set(input.pop(0).split())
    cards2[3] = set(input.pop(0).split())
    cards2[4] = set(input.pop(0).split())
    
    res = cards2[row2] & cards1[row1]
    if len(res) == 0:
        print "Case #%d: Volunteer cheated!" % (i+1,)
    elif len(res) > 1:
        print "Case #%d: Bad magician!" % (i+1,)
    else:
        print "Case #%d: %s" % (i+1, [card for card in res][0])


    