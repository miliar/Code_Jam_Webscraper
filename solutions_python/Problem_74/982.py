#Tested locally with Python 2.6.6 on OS X 10.6.7
import math

input = open('A-large.in','r')
output = open('A-large.out','w')
T = int(input.next())

for i in range(0,T):
    numsonein = input.next().split(' ')
    orangePos = 1
    bluePos = 1
    time = 0
    timeSinceSwitch = 0

    N = int(numsonein[0])
    lastBot = ''
    for j in range(0,N):
        curBot = numsonein[(2*j)+1]
        curBut = int(numsonein[(2*j)+2])
    
        if curBot == lastBot:
            getTime = 0
        else:
            getTime = timeSinceSwitch

        if curBot == 'O':
            timeMoving = max(0,abs(orangePos-curBut)-getTime)
            orangePos = curBut
        if curBot == 'B':    
            timeMoving = max(0,abs(bluePos-curBut)-getTime)
            bluePos = curBut

        time = time+timeMoving+1
        if curBot == lastBot:
            timeSinceSwitch = timeSinceSwitch + timeMoving + 1
        else:
            timeSinceSwitch = timeMoving + 1
        
        lastBot = curBot

    output.write("Case #"+str(i+1)+": "+str(time)+"\n")
