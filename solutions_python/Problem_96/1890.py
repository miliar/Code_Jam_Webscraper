import io
import sys

with io.open(sys.stdin.fileno()) as stdin:
    numCases = int(stdin.readline())
    for case in range(1, numCases+1):
        numbers = stdin.readline().split()
        googlers = int(numbers[0])
        maxSurprising = int(numbers[1])
        minPoints = int(numbers[2])
        numNotSurprising = 0
        numSurprising =0
        for googler in range(3,googlers+3):
            points = int(numbers[googler])
            if points == 1 and minPoints == 1:
                numNotSurprising +=1
            elif (points == 2 or points==3) and minPoints ==2:
                numSurprising+=1
            elif points >= 3*minPoints-2:
                numNotSurprising+=1
            elif points >= 4 and points >= 3*minPoints-4:
                numSurprising+=1
        result = numNotSurprising + min(maxSurprising, numSurprising)
        
        print("Case #%d: %d" %(case,result))
        
