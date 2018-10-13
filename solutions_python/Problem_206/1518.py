import sys
import os
import re
sys.setrecursionlimit(50000)

def getHorseDes(desHorseString):
    words = desHorseString.split()
    return words
    
def getHorseTime(horseString, destiny):
    words = horseString.split()
    distance = destiny - int(words[0])
    time = distance / int(words[1])
    return time
def main():
    # open and read input file
    content = []
    with open("input.txt") as f:
        content = f.read().splitlines()

        # get first line number as number of iterations
        iterateNum = int(content[0])
        horseNumber = 0
        desNumber = 0
        currentLineNum = 0

    # get each line of test string
    for i in range(1, iterateNum + 1):
        currentLineNum += horseNumber + 1
        print("Case #" + str(i) + ": ", end = "")
        desHorseString = content[currentLineNum]
        list = getHorseDes(desHorseString)
        desNumber = int(list[0])
        horseNumber = int(list[1])
        maxHour = 0
        for j in range(1, horseNumber + 1):
            if maxHour < getHorseTime(content[currentLineNum + j], desNumber):
                maxHour = getHorseTime(content[currentLineNum + j], desNumber)
        speed = desNumber/maxHour
        print("%.6f" % speed)
            
            
        # clode input file
        f.close()
  
  
# calling main function  
main()