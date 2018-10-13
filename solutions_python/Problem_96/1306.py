with open('b.in', 'r') as fin:
    with open('b.out', 'w') as fout:
        cases = int(fin.readline())
        for i in range(cases):
            danceline = fin.readline().split()
            googlers = int(danceline[0])
            surprises = int(danceline[1])
            p = int(danceline[2])
            goodGoogler = 0
            potentialSurprise = 0
            for j in range(googlers):
                if (p >= 2):
                    if (int(danceline[j+3]) >= p*3-2):
                        goodGoogler += 1
                    elif (int(danceline[j+3]) >= p*3-4):
                        potentialSurprise += 1
                elif (p == 1):
                    if (int(danceline[j+3]) > 0):
                        goodGoogler += 1
                else:
                    goodGoogler += 1
                
            fout.write('Case #' + str(i+1) + ': ' + str(min(goodGoogler+potentialSurprise, goodGoogler+surprises))+ '\n');
            