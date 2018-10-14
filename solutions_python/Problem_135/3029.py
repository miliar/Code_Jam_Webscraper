def magicTrick():
    infile = open("A-small-attempt0.in", 'r')
    outfile = open("answer.txt", 'w')
    cases = int(infile.readline())
    for case in range(cases):
        set1 = [[''] for i in range(4)]
        set2 = [[''] for i in range(4)]
        
        guess1 = int(infile.readline().rstrip())
        for i in range(4):
            set1[i] = infile.readline().rstrip().split(' ')
        guess2 = int(infile.readline().rstrip())
        for i in range(4):
            set2[i] = infile.readline().rstrip().split(' ')

        potential = 0
        answers = []
        for num in set1[guess1-1]:
            if num in set2[guess2-1]:
                potential += 1
                answers.append(num)

        if potential == 1:
            outfile.write("Case #" + str(case+1) + ": " + answers[0])
        elif potential > 1:
            outfile.write("Case #" + str(case+1) + ": Bad magician!")
        elif potential == 0:
            outfile.write("Case #" + str(case+1) + ": Volunteer cheated!")
        if case != cases-1:
            outfile.write("\n")

magicTrick()
