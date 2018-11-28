
import math
import sys
#import random

max = 10000

def getCell(row,col):
    if (row<0 or row>=H or col<0 or col>=W):
        return -1
    else:
        return altMap[row][col]
        
def matrixToString(m):
    result = "\n"
    for i in range(0,H):
        for j in range(0,W):
            result += m[i][j]
            if (j<W-1):
                result += " "
        if (i<H-1):
            result += "\n"
    return result
    

def getDrainMap():
    resultMap = []
    for i in range(0,H):
        emptyRow = [' '] * W
        resultMap.append(emptyRow)
    currentChar = 0
    allChars = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0,H):
        for j in range(0,W):
            row = i
            col = j
            drained = False
            while resultMap[row][col]==' ' and not drained:
                resultMap[row][col] = '.'
                # Check where this cell drains to, mark advancement. Preference is N, W, E, S
                winnerVal = getCell(row,col)
                winnerRow = row
                winnerCol = col
                cand = getCell(row-1,col) 
                if (cand>=0 and cand<winnerVal):
                    winnerVal = cand
                    winnerRow = row-1
                    winnerCol = col
                cand = getCell(row,col-1)
                if (cand>=0 and cand<winnerVal):
                    winnerVal = cand
                    winnerRow = row
                    winnerCol = col-1
                cand = getCell(row,col+1)
                if (cand>=0 and cand<winnerVal):
                    winnerVal = cand
                    winnerRow = row
                    winnerCol = col+1
                cand = getCell(row+1,col)
                if (cand>=0 and cand<winnerVal):
                    winnerVal = cand
                    winnerRow = row+1
                    winnerCol = col
                if (row == winnerRow and col == winnerCol):
                    drained = True
                # move on to next place...
                row = winnerRow
                col = winnerCol
            if (resultMap[row][col]=='.'):
                # This was a new draining path, mark it with next available char
                markChar = allChars[currentChar]
                currentChar += 1
            else:
                # found an existing draining point
                markChar = resultMap[row][col]
            for row in range(0,H):
                for col in range(0,W):
                    if resultMap[row][col]=='.':
                        resultMap[row][col]=markChar
    return matrixToString(resultMap)

def processFile(source, target):
    global H
    global W
    global altMap
    sf = open(source)
    tf = open(target,"w")
    T = sf.readline()
    T = int(T)
    for case in range(1, T+1):
        [H,W] = sf.readline().strip('\n').split(' ')
        H = int(H)
        W = int(W)
        altMap = []
        for rowIndex in range(0,H):
            row = sf.readline().strip('\n').split(' ')
            for i in range(0,len(row)):
                row[i] = int(row[i])
            altMap.append(row)
        result = getDrainMap()
        newline = 'Case #' + str(case) + ': ' + result
        tf.write(newline)
        if not case==T: tf.write('\n')
    sf.close
    tf.close


def main(argv = None):
    if argv is None:
        argv = sys.argv
    if (len(argv)>2):
        processFile(argv[1], argv[2])
    
if __name__ == "__main__":
    main()
    