import sys

def getrow(infile):
    target = int(infile.readline())
    row = None
    for rownum in range(1, 5):
        thisrow = [int(x) for x in infile.readline().split()]
        if rownum == target: row = thisrow
    assert row is not None
    return row

def run_case(casenum, infile):
    r1 = getrow(infile)
    r2 = getrow(infile)
    cards = []
    for card in r1:
        if card in r2:
            cards.append(card)
    if len(cards) == 0:
        result = "Volunteer cheated!"
    elif len(cards) == 1:
        result = "%s" % cards[0]
    elif len(cards) > 1:
        result = "Bad magician!"

    print "Case #%d: %s" % (casenum, result)
    
infile = open(sys.argv[1], "r")

numcases = int(infile.readline())

for casenum in range(1, numcases + 1):
    run_case(casenum, infile)

