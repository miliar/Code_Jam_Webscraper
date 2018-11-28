with open("A-small-attempt0.in", "rt") as in_file:
    with open("out.txt", "wt") as out_file:
        runs = in_file.readline()
        runs = int(runs)
        for run in range(1,(runs+1)):
            cardRow=int(in_file.readline())
            for row in range(1,5):
                cards=in_file.readline()
                if row == cardRow:
                    possibleCards=[int(i) for i in cards.split(' ')]
            cardRow=int(in_file.readline())
            for row in range(1,5):
                cards=in_file.readline()
                if row == cardRow:
                    otherPossibleCards=[int(i) for i in cards.split(' ')]
            if len(set(possibleCards)&set(otherPossibleCards))== 1:
                out_file.write("Case #"+str(run)+": "+str((set(possibleCards)&set(otherPossibleCards)).pop())+"\n")
            elif len(set(possibleCards)&set(otherPossibleCards))== 0:
                out_file.write("Case #"+str(run)+": "+"Volunteer cheated!\n")
            else:
                out_file.write("Case #"+str(run)+": "+"Bad magician!\n")
