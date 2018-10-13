# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 15:51:02 2014

@author: HDB
Google codejam
"""
import numpy

def getArray(size):
    data = []
    for i in xrange(size):
        row = raw_input()
        rowData = [int(x) for x in row.split()]
        data += rowData
    return data

def handleInput():
    numCases = int(raw_input())
    firsts = []
    seconds = []
    indices = []
    if numCases >0:
        for i in xrange(numCases):
            ind1 = int(raw_input())
            firstData = getArray(4)
            firstArr = numpy.array(firstData)
            firstArr.shape = (4,4)
            
            ind2 = int(raw_input())
            secondData = getArray(4)
            secondArr = numpy.array(secondData)
            secondArr.shape = (4,4)
            
            indices.append((ind1, ind2))
            firsts.append(firstArr)
            seconds.append(secondArr)
    return firsts, seconds, indices
    
def getArr(lines, start, size):
    data = []
    for i in xrange(size):
        row = lines[start+i]
        rowData = [int(x) for x in row.split()]
        data += rowData
    return data
    
def handleFileInput():
    fname = "A-small-attempt1.in"
    f = open(fname, "rb")
    lines = f.readlines()
    f.close()
    #numCases = int(lines[0])
    firsts = []
    seconds = []
    indices = []
    for sectStart in xrange((len(lines)-1)/10):
        sectStart = sectStart*10 + 1

        ind1 = int(lines[sectStart])
        firstData = getArr(lines, sectStart+1, 4)
        firstArr = numpy.array(firstData)
        firstArr.shape = (4,4)
        
        ind2 = int(lines[sectStart+5])
        secondData = getArr(lines, sectStart+6, 4)
        secondArr = numpy.array(secondData)
        secondArr.shape = (4,4)
        indices.append((ind1, ind2))
        firsts.append(firstArr)
        seconds.append(secondArr)
        
    return firsts, seconds, indices
    
    
def game(first, second, indices):
    
    firstRow = set(first[indices[0] -1, :])

    secondRow= set(second[indices[1]-1,:])

    possibleCards = firstRow.intersection(secondRow)
    numberCards = len(possibleCards)
    
    if numberCards == 1:
        result = possibleCards.pop()
    elif numberCards == 0:
        result = "Volunteer cheated!"
    else:
        result = "Bad magician!"
    return result




def main():
    firsts, seconds, indices = handleFileInput()
    fname = "output.txt"
    fout  = open(fname, "wb");
    
    for index, value in enumerate(firsts):
        result = game(value, seconds[index], indices[index])
        output = "Case #" + str(index+1) + ": " + str(result)
        fout.write(output + "\n")
    fout.close()
        
if __name__=="__main__":
    main()


                