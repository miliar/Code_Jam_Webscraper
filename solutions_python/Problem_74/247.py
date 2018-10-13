import sys,math

numOfTests= int(sys.stdin.readline())
for t in range(1,numOfTests+1):
    line = sys.stdin.readline().split()
    #put buttons into O an B
    numButtons = int(line[0])
    O = []
    B = []
    order = []
    for j in range(1,numButtons*2):
        if line[j] == 'O':
            O.append(int(line[j+1]))
            order.append(['O',int(line[j+1])])
        if line[j] == 'B':
            B.append(int(line[j+1]))
            order.append(['B',int(line[j+1])])
    
    runTime = 0
    timeSinceLastB = 0
    timeSinceLastO = 0
    lastO = 1
    lastB = 1
    
    for o in order:
        bot = o[0]
        button = o[1]
        if bot == 'O':
            runTime = runTime + abs(button  - lastO) - min(timeSinceLastO , abs(button  - lastO)) + 1
            timeSinceLastB = timeSinceLastB + abs(button  - lastO) - min(timeSinceLastO , abs(button  - lastO)) + 1
            timeSinceLastO = 0
            lastO = button
        if bot == 'B':
            runTime = runTime + abs(button  - lastB) - min(timeSinceLastB , abs(button  - lastB)) + 1
            timeSinceLastO = timeSinceLastO + abs(button  - lastB) - min(timeSinceLastB , abs(button  - lastB)) + 1
            timeSinceLastB = 0
            lastB = button
            
    print "Case #" + str(t) + ": " + str(runTime)
        

    