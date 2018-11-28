fInput = file('A-large.in', 'r')
fOutput = file('A-large.out', 'w')

caseNum = int(fInput.readline())
for case in range(0, caseNum):
    firstLine = fInput.readline().split()
    P = int(firstLine[0])
    K = int(firstLine[1])
    L = int(firstLine[2])
      
    press = fInput.readline().split()
    numPress = []
    for c in press:
        numPress.append(int(c))
        
    numPress.sort(reverse=True)
    
    pressNum = 0
    index = 0
    for i in range(0, P):
        if (index == len(press)):
            break
        for j in range(0, K):
            pressNum += (i + 1) * numPress[index]
            index += 1
            if (index == len(press)):
                break
            
    fOutput.write('Case #%d: %d\n' % (case + 1, pressNum))
        
fOutput.close()
fInput.close()

