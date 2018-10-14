def readCards(f):
    l = f.readline()
    volunteer_choice = int(l)
    rows = [0] * 4
    for cards in range(4):
        l = f.readline().split()
        rows[cards] = [int(x) for x in l]
    return (volunteer_choice, rows)
    

with open("A-small-attempt1.bin", "r") as f:
    cases = int(f.readline())
    for i in range(cases):
        order1 = readCards(f)
        choice1 = order1[0]
        order2 = readCards(f)
        choice2 = order2[0]
        poss = []
        for c in order1[1][choice1 - 1]:
            if c in order2[1][choice2 - 1]:
                poss.append(c)
        
        msg = "Case #%d: " % (i + 1)
        if len(poss) == 1:
            msg += str(poss[0])
        elif len(poss) == 0:
            msg += "Volunteer cheated!"
        elif len(poss) > 1:
            msg += "Bad magician!"
                
        print(msg)



