import sys

infile = sys.stdin

T = int(infile.readline())
for case in xrange(T):
    firstAnswer = int(infile.readline().split()[0])
    firstCards = []
    for j in range(4):
        firstCards.append(infile.readline().split())
    secondAnswer = int(infile.readline().split()[0])
    secondCards = []
    for j in range(4):
        secondCards.append(infile.readline().split())

    selectedCard = []    
    for card in firstCards[firstAnswer-1]: 
        if card in secondCards[secondAnswer-1]:
            selectedCard.append(card)

    if len(selectedCard) == 1:
        result = selectedCard[0]
    if len(selectedCard) >1:
        result = "Bad magician!"
    if len(selectedCard) == 0:
        result = "Volunteer cheated!"

    #print sequence
    print("Case #%d: %s" % (case+1, result))