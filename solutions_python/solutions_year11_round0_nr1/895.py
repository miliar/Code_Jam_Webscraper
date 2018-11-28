# -*- coding: UTF-8 -*-
#!/usr/bin/env python

inputName  = 'A-large.in'
outputName = 'output.txt'

def main():
    print("Google Code Jam:\nBot Trust")
    inputFile  = open(inputName, 'r')
    outputFile = open(outputName, 'w')
    nmrCases = int(inputFile.readline().rstrip()) #количество вариантов
    print("nmrCases =", nmrCases)
    for case in range(nmrCases):
        time = 0 #счетчик времени
        bluePosition   = 1 #позиция оранжевого робота
        orangePosition = 1 #позиция оранжевого робота
        preRobotTime   = 0
        buttonSequence = inputFile.readline().rstrip().split()
        nmrButton = int(buttonSequence[0])
        preRobot = buttonSequence[1]
        print("\ncase =", case + 1)
        print("nmrButton =", nmrButton)
        print("buttonSequence =", buttonSequence)
        for i in range(1, nmrButton+1):
            robot = buttonSequence[i*2-1]
            print("robot =", robot, "button =", buttonSequence[i*2])
            #print("button =", buttonSequence[i*2])
            if robot == 'O':
                delta = (int(buttonSequence[i*2]) - orangePosition)
                orangePosition += delta
                delta = abs(delta)
                if robot != preRobot:
                    if preRobotTime < delta:
                        delta = delta - preRobotTime
                    elif preRobotTime >= delta:
                        delta = 0
                    preRobotTime = 0
                time += delta + 1
                preRobotTime += delta + 1
                print("preRobotTime =", preRobotTime)
                print("orangePosition =", orangePosition)
                print("time =", time)
            if robot == 'B':
                delta = (int(buttonSequence[i*2]) - bluePosition)
                bluePosition += delta
                delta = abs(delta)
                if robot != preRobot:
                    if preRobotTime < delta:
                        delta = delta - preRobotTime
                    elif preRobotTime >= delta:
                        delta = 0
                    preRobotTime = 0
                time += delta + 1
                preRobotTime += delta + 1
                print("preRobotTime =", preRobotTime) 
                print("bluePosition =", bluePosition)
                print("time =", time)
            preRobot = robot
        outputFile.write("Case #" + str(case+1) + ": " + str(time) + "\n")
    inputFile.close()
    outputFile.close()
    print("Done")

if __name__ == '__main__':
    main()