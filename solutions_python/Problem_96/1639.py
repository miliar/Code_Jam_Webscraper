def googleDancer(filename):
    f = file(filename, 'r')
    lines = f.readlines()
    caseNumber = lines[0]
    lines = lines[1:]
    myOutput = ''
    caseCount = 1
    
    for line in lines:
        myLine = line.split()
        N = int(myLine[0])
        S = int(myLine[1])
        p = int(myLine[2])
        scores = myLine[3:]

        total = 0
        
        for num in scores:
            myNum = int(num)
            left = myNum - p - (p-1)
            surp = myNum - p - (p-2)
            if p == 0:
                total  = total + 1
            elif left>=(p-1) and (p-1)>=0:
                total = total + 1
            elif surp >= (p-2) and not(S == 0) and (p-2)>=0:
                total = total + 1
                S = S - 1
            
        myOutput = myOutput + 'Case #' + str(caseCount) + ': ' + str(total) + '\n'
        caseCount = caseCount + 1
    
    #print myOutput
    out = file('myOutput.txt', 'w')
    out.write(myOutput)
