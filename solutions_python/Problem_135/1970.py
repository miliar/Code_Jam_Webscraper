count = int(raw_input())
magicTrick = []
case = []

for i in range(count*10):
    magicTrick.append(raw_input())

for i in range(0,count*10,10):
    firstCard = []
    secondCard = []
    cards = []
    for m in range(10):
        if m == 0:
            first = int(magicTrick[i+m])-1
        elif m == 5:
            second = int(magicTrick[i+m])-1
        elif m > 0 and m < 5:
            firstCard.append(magicTrick[i+m].split())
        elif m > 5 and m < 10:
            secondCard.append(magicTrick[i+m].split())

    for a in firstCard[first]:
        for b in secondCard[second]:
            if a == b:
                if a not in cards:
                    cards.append(a)
    
    l = len(cards)
    if l == 1:
        case.append(cards[0])
    elif l == 0:
        case.append("Volunteer cheated!")
    elif l > 1:
        case.append("Bad magician!")

for i in range(count):
    print "Case #"+str(i+1)+": "+case[i]

