a_file = open('A-large.in')
numcases = int(a_file.readline())



for caseNum in range(numcases):
    
    param = a_file.readline().split()
    numInstr = int(param[0])

    posO = 1
    posB = 1
    
    score = 0
    for i in range(numInstr):
        currentBot = param[2*i + 1]
        for j in range(i, numInstr):
            desiredO = 0
            if param[2*j + 1] == "O":
                desiredO = int(param[2*j + 2])
                break
            
        for k in range(i, numInstr):
            desiredB = 0
            if param[2*k + 1] == "B":
                desiredB = int(param[2*k + 2])
                break

        if currentBot == "O":
            while posO != desiredO:
                if posO < desiredO:
                    posO += 1
                if posO > desiredO:
                    posO -= 1
                if posB < desiredB:
                    posB += 1
                if posB > desiredB:
                    posB -= 1
                score += 1
            if posB < desiredB:
                posB += 1
            if posB > desiredB:
                posB -= 1
            score += 1
        elif currentBot == "B":
            while posB != desiredB:
                if posO < desiredO:
                    posO += 1
                if posO > desiredO:
                    posO -= 1
                if posB < desiredB:
                    posB += 1
                if posB > desiredB:
                    posB -= 1
                score += 1
            if posO < desiredO:
                posO += 1
            if posO > desiredO:
                posO -= 1
            score += 1
        else:
            print("shiould not happen")

        
        
    
    print("Case #" + str(caseNum + 1) + ": " + str(score))
