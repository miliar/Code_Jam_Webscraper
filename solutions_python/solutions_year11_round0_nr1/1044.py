
f = open('A-large.in', 'r')
out = open('largeoutput.txt', 'w')

numLines = int(f.readline())

for i in range(numLines):
    
    orangeSequence = []
    blueSequence = []
    order = []
    
    vals = f.readline().split(' ')
    
    numVals = int(vals[0])
    
    for j in range(numVals):
        order.append(vals[j*2 + 1])
        if(vals[j*2 + 1] == 'O'):
            orangeSequence.append(int(vals[j*2 + 2]))
        else:
            blueSequence.append(int(vals[j*2 + 2]))
    
    orangeIndex = 0
    orangePosition = 1  # Current position
    orangeButton = 0    # Is it on the button?
    
    blueIndex = 0
    bluePosition = 1
    blueButton = 0
    
    orderIndex = 0
    totalSeconds = 0
    
    orangeDone = False
    blueDone = False
    
    #print order
    
    while(orderIndex < len(order)):
        
        if(orangeIndex >= len(orangeSequence)):
            orangeDone = True
        else:
            orangeTarget = orangeSequence[orangeIndex]
            
        if(blueIndex >= len(blueSequence)):
            blueDone = True
        else:
            blueTarget = blueSequence[blueIndex]
        
        pushed = False
        
        if(not orangeDone):
            if(orangePosition < orangeTarget):
                # Move forward
                orangePosition += 1
            elif(orangePosition > orangeTarget):
                # Move back
                orangePosition -= 1
            elif(order[orderIndex] == 'O'):
                # It's your turn, push the button!
                pushed = True
                orangeIndex += 1
            # Else wait
            
        if(not blueDone):
            if(bluePosition < blueTarget):
                # Move forward
                bluePosition += 1
            elif(bluePosition > blueTarget):
                # Move back
                bluePosition -= 1
            elif(order[orderIndex] != 'O'):
                # It's your turn, push the button!
                pushed = True
                blueIndex += 1
            # Else wait
        
        if(pushed):
            orderIndex += 1
        
        totalSeconds += 1
        #print '%d, %d, %d' % (orangePosition, bluePosition, totalSeconds)
    
    print('Case #%d: %d\n' % (i+1, totalSeconds))
    out.write('Case #%d: %d\n' % (i+1, totalSeconds))

f.close()
out.close()