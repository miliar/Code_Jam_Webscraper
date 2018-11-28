with open('output.txt','w') as o:
    with open('A-small-attempt0.in','r') as f:
        lines = f.readlines()
        T = int(lines[0])
        #linesPerCase = 10
        for Tnum in range(0,T):
            answer1 = int(lines[1+10*Tnum])
            answer2 = int(lines[6+10*Tnum])
            row1 = lines[answer1+1+10*Tnum]
            row2 = lines[answer2+6+10*Tnum]
            
            numPossibleCards = 0
            for card1 in row1.split():
                for card2 in row2.split():
                    if card1==card2:
                        answer = card1
                        numPossibleCards = numPossibleCards + 1

            o.write('Case #' + str(Tnum+1) + ': ')
            if numPossibleCards == 0:
                o.write('Volunteer cheated!\n')
            if numPossibleCards == 1:
                o.write(str(answer)+'\n')
            if numPossibleCards > 1:
                o.write('Bad magician!\n')
                
            
