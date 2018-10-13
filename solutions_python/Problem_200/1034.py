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
def isAscending(num):
    ascending = True
    numList = list(str(num))
    for i in range(len(numList) - 1):
        if (numList[i] > numList[i + 1]):
            ascending = False

    return ascending

def findNum(num):
    numList = list(str(num))

    while (not isAscending(num)):
        for i in range(len(numList) - 1):
            if (numList[i] > numList[i + 1]):
                digit = int(numList[i])
                newDigit = digit - 1
                if newDigit < 0:
                    newDigit = 9
                numList[i] = str(newDigit)

                for j in range(len(numList) - (i + 1)):
                    numList[i + j + 1] = "9"

                num = int(''.join(numList))

    return num
'''--------------------------------------'''

'''--------------Main block--------------'''
readInput()  # Read the whole input data input
testsCount = int(readNextLine())  # Read the tests count

for n in range(testsCount):
    split_words = readNextLine().split()

    '''Do something with data'''
    num = int(split_words[0])
    correntNum = findNum(num)
    resultString = str(correntNum)
    '''----------------------'''

    out_lines.append("Case #" + str(n + 1) + ": " + resultString)  # Save data result
    
saveOutput()  # Save the whole output data input
'''--------------------------------------'''