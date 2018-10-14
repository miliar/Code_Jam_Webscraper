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
def turnBunch(pancakes, n, pos):
    for i in range(n):
        if pancakes[pos + i] == "-":
            pancakes[pos + i] = "+"
        elif pancakes[pos + i] == "+":
            pancakes[pos + i] = "-"

def pancakesTurner(pancakes, n):
    #print "new", pancakes
    flips = 0
    length = len(pancakes) - n + 1
    for i in range(length):
        if pancakes[i] == "-":
            turnBunch(pancakes, n, i)
            flips += 1
            #print pancakes

    if not checkIsDone(pancakes):
        flips = -1

    return flips

def checkIsDone(pancakes):
    done = True
    for i in pancakes:
        if i == "-":
            done = False
    return done
'''--------------------------------------'''


'''--------------Main block--------------'''
readInput()  # Read the whole input data input
testsCount = int(readNextLine())  # Read the tests count

for n in range(testsCount):
    split_words = readNextLine().split()

    '''Do something with data'''
    pancakes = list(split_words[0])
    num = int(split_words[1])
    flips = pancakesTurner(pancakes, num)

    if flips == -1:
        resultString = "IMPOSSIBLE"
    else:
        resultString = str(flips)
    '''----------------------'''

    out_lines.append("Case #" + str(n + 1) + ": " + resultString)  # Save data result
    
saveOutput()  # Save the whole output data input
'''--------------------------------------'''