T = int(raw_input())
for t in range(T):
    command = raw_input().split()[1:]
    
    robots = command[::2]
    buttons = map(int, command[1::2])
    
    oPos , bPos = 1, 1
    lastO, lastB = 0,0
    timeElapsed = 0
    for robot, button in zip(robots, buttons):
#        print "Robot, Button:", robot, button
        if robot == 'O':
            moveTime = abs(oPos - button) - (timeElapsed - lastO) # calculate the time needed to move
#            print "Movetime:", moveTime
            if moveTime >= 0:
                timeElapsed += moveTime + 1
            else:
                timeElapsed += 1
#            print "TimeElapsed: ", timeElapsed
            lastO = timeElapsed
#            print "lastO:" , lastO
            oPos = button
#            print "oPos:", oPos
        else:
            moveTime = abs(bPos - button) - (timeElapsed - lastB) # calculate the time needed to move
#            print "Movetime:", moveTime
            if moveTime >= 0 :
                timeElapsed += moveTime + 1
            else:
                timeElapsed += 1
#            print "TimeElapsed: ", timeElapsed
            lastB = timeElapsed
#            print "lastB:" , lastB
            bPos = button
#            print "bPos:", bPos            
    print "Case #%d: %d" %(t+1,  timeElapsed)

