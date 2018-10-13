f = open("A-small-attempt0.in", 'r')
w = open("smalA.txt", 'w')
cnt = 0
lines = f.readlines()
numCases = int(lines[0])
for i in range(0, numCases):
    n = i*10
    guess1 = int(lines[n+1])
    guess2 = int(lines[n+1+5])
    row1 = lines[n+1+guess1].split()
    row2 = lines[n+1+5+guess2].split()

    badMagician = False
    cardChosen = -1
    for j in row1:
        for k in row2:
            if (j == k):
                if (cardChosen != -1):
                    badMagician = True
                    break
                else:
                    cardChosen = j
    print str(cardChosen), str(badMagician)
    if badMagician:
        print >> w, "Case #" + str(i+1) + ": Bad magician!"
    elif cardChosen == -1:
        print >> w, "Case #" + str(i+1) + ": Volunteer cheated!"
    else:
        print >> w, "Case #" + str(i+1) + ": " + str(cardChosen)
