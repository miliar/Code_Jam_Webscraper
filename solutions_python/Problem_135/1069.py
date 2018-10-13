def magictrick(f):
    T = int(f.readline())
    testcase = 0
    while testcase < T:
        # First Guess
        guess = int(f.readline())
        
        for rows in range(0, guess):
            firstrow = f.readline().split()
        leftover = 4 - guess
        
        if leftover > 0:
            for i in range(0,leftover):
                f.readline() # throw away the leftover
        
        # Second Guess
        guess = int(f.readline())
        for rows in range(0, guess):
            secondrow = f.readline().split()
        
        leftover = 4 - guess
        if leftover > 0:
            for i in range(0,leftover):
                f.readline()
                
        
        thenumber = filter(lambda x: x in firstrow, secondrow)
        
        decision = "Case #" + str(testcase+1) + ": "
        if len(thenumber) == 1:
            decision = decision + thenumber[0]
        elif len(thenumber) > 1:
            decision = decision + "Bad magician!"
        else:
            decision = decision + "Volunteer cheated!"
        
        output = open('output','a')
        output.write(decision+"\n")
        output.close
        
        testcase += 1
    
    
      
    

f = open('A-small-attempt0.in')
magictrick(f)