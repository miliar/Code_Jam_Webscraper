'''
Created on Apr 12, 2013

@author: kai
'''
import sys
from scipy import *

def deleteRow(matrix,rowIndex):
    return delete(matrix,rowIndex,0)

def deleteColumn(matrix,columnIndex):
    return delete(matrix,columnIndex,1)

def checkSmallest(row,value):
    allSameAsValue = True
    for item in row:
        if item != value:
            allSameAsValue = False
    return allSameAsValue
    
def downSizeLawn(lawn):
    '''find smallest value '''
    smallestValue = 100
    
    for row in lawn:
        for item in row:
            if item<smallestValue:
                smallestValue = item
    '''find straight line of the smallestValue'''
    
    indexOfSmallestRow = -1
    indexOfSmallestColumn = -1 
    
    rowIndex = 0
    for row in lawn:
        if checkSmallest(row,smallestValue):
            indexOfSmallestRow = rowIndex
        rowIndex += 1
    
    for columnIndex in range(0,len(lawn[0])):
        column = zeros(len(lawn))
        for rowIndex in range(0,len(lawn)):
            column[rowIndex] = lawn[rowIndex][columnIndex]
        if checkSmallest(column,smallestValue):
            indexOfSmallestColumn = columnIndex
    
    if(indexOfSmallestRow >=0 ):
        lawn = deleteRow(lawn,indexOfSmallestRow)
        return True,lawn
    elif(indexOfSmallestColumn >=0 ):    
        lawn = deleteColumn(lawn,indexOfSmallestColumn)
        return True,lawn
    else:
        return False,lawn
    
    
if __name__ == '__main__':
    hndlin = open(sys.argv[1],'rt')
    hndlout = open(sys.argv[2],'w')
    
    numberCases = int(hndlin.readline())
    
    for index in range(0,numberCases):

        N,M = hndlin.readline().rstrip('\n').split(' ')
        N = int(N)
        M = int(M)
        lawn = zeros([N,M])
        
        for row in range(0,N):
            line = hndlin.readline().rstrip('\n').split(' ')
            for column in range(0,M):
                lawn[row][column] = int(line[column]) 
        
        while True:
            beingDownSized,lawn = downSizeLawn(lawn)
            if beingDownSized == False or len(lawn) == 0:
                break
            
        if len(lawn)==0:
            output = "Case #"+str(index+1)+": "+ "YES" + '\n'
        else:
            output = "Case #"+str(index+1)+": "+ "NO" + '\n'
        print output
        hndlout.write(output)
        
    hndlin.close()
    hndlout.close()