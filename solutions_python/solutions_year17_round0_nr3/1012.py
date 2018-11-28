import math
from math import *
 
in_lines = []
in_pos = 0
out_lines = []

'''------------Read data block-----------'''
def readInput():
    global in_lines
    with open('test.in') as f:
        in_lines = f.readlines()

def saveOutput():
    global out_lines
    text_file = open("test.out", "w")
    for s in out_lines:
        text_file.write(s + '\n')
    text_file.close()

def readNextLine():
    global in_pos
    in_pos += 1
    return in_lines[in_pos - 1].replace("\n", "")
'''--------------------------------------'''

'''---------Data analysing block---------'''

def findDistances(stalls, people):
    currentSegments = 1
    currentLargeSegmentsLength = stalls
    currentLargeSegmentsCount = 1

    stallMaxDist = 0
    stallMinDist = 0

    peopleForSegments = 0
    acquipiedLargeSegmentsCount = 0
    for i in range(people):
        peopleForSegments += 1

        if (acquipiedLargeSegmentsCount < currentLargeSegmentsCount):
            stallMaxDist = int(math.ceil((currentLargeSegmentsLength - 1) / 2.0))
            stallMinDist = int(math.floor((currentLargeSegmentsLength - 1) / 2.0))
            acquipiedLargeSegmentsCount += 1
        else:
            currentSmallSegmentsLength = currentLargeSegmentsLength - 1
            stallMaxDist = int(math.ceil((currentSmallSegmentsLength - 1) / 2.0))
            stallMinDist = int(math.floor((currentSmallSegmentsLength - 1) / 2.0))


        if (peopleForSegments == currentSegments):
            newSegments = currentSegments * 2

            if (newSegments == 2):
                if currentLargeSegmentsLength % 2 == 1:
                    currentLargeSegmentsCount = 2
                else:
                    currentLargeSegmentsCount = 1
            else:
                if currentLargeSegmentsLength % 2 == 1:
                    smallSegmentsCount = (currentSegments - currentLargeSegmentsCount)
                    newLargeSegmentsCount = smallSegmentsCount + currentLargeSegmentsCount * 2
                    currentLargeSegmentsCount = newLargeSegmentsCount
                else:
                    currentLargeSegmentsLength = currentLargeSegmentsLength

            if currentLargeSegmentsLength % 2 == 0:
                currentLargeSegmentsLength = int(currentLargeSegmentsLength / 2)
            else:
                currentLargeSegmentsLength = int((currentLargeSegmentsLength - 1) / 2)

            currentSegments *= 2
            peopleForSegments = 0
            acquipiedLargeSegmentsCount = 0

    return [stallMaxDist, stallMinDist]
'''--------------------------------------'''

'''--------------Main block--------------'''
readInput()  # Read the whole input data input
testsCount = int(readNextLine())  # Read the tests count

for n in range(testsCount):
    split_words = readNextLine().split()

    '''Do something with data'''
    stalls = int(split_words[0])
    people = int(split_words[1])

    res = findDistances(stalls, people)

    resultString = str(res[0]) + " " + str(res[1])
    '''----------------------'''

    out_lines.append("Case #" + str(n + 1) + ": " + resultString)  # Save data result
    
saveOutput()  # Save the whole output data input
'''--------------------------------------'''