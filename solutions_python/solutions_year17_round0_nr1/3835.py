# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 20:43:48 2017

@author: annaparker
"""

def readFile(): 
    """reads input"""
    input = []
    x = 0
    with open("input.in") as file:
        for line in file: #ignore first line, integer isn't used
            if(x == 0):
                x = 1 
            else:
                a = line.partition(' ')
                input += [a]
    return input


def removeHappySideUp(panLine):
    """Starting at leftmost pancake, removes consecutive happy side up pancakes (+)."""
    while(len(panLine) > 0 and panLine[0] == '+'):
        panLine = panLine[1:]               
    return panLine
    
    
    
    
def flip(flipperSize, currPancake):
    """flips leftmost pancakes using giant flipper"""    
    for i in range(0, flipperSize):
        if(currPancake[i] == '+'):
            currPancake[i] = '-'
        else:
            currPancake[i] = '+'
    

    return currPancake


    

def theBigFlip(flipLen, pancakes):
    """
    counts number of flips required given a line of pancakes and a flipper of size flipLen, or states it is impossible.
    runs by continually moving left to right on line, removing all completed pancakes then flipping leftmost pancakes using big flipper.
    this loop will end with either a list of 0 pancakes (all happy, return count), a list of flipLen pancakes (if all pancakes are blank return counter + 1, otherwise impossible), or a list of pancakes that includes blank sides but is too short to be flipped (impossible).             
    """
    flipCounter = 0
    pancakes = removeHappySideUp(pancakes)
    
    while(len(pancakes) > flipLen):
        pancakes = flip(flipLen, pancakes)
        flipCounter += 1
        pancakes = removeHappySideUp(pancakes)
    
    if len(pancakes) == 0: #all pancakes are successfully happy side up!
        return flipCounter 

    if len(pancakes) == flipLen:
        for i in range (0, len(pancakes)):
            if(pancakes[i] == '+'): #final flip won't result in all pancakes happy side up
                return 'IMPOSSIBLE'
                
        return flipCounter + 1 #only one more flip required to make all pancakes happy side up!
        
    else: #remaining line too short to be flipped & contains blank pancakes 
        return 'IMPOSSIBLE'





def write(output):
    """write output to file"""
    target = open('out.in', 'w')
    count = 1
    for element in output:     
        target.write("Case #%s: %s\n" % (count, element))
        count += 1
        
    target.close()
    
    

#collect input
inputList = readFile()
flipCounts = []


for element in inputList:
    flipperLength = int(element[2])
    pancakeLine = list(element[0])

    #returns either number of flips or that given length/line combination is impossible
    flipCounts += [theBigFlip(flipperLength, pancakeLine)]


write(flipCounts)