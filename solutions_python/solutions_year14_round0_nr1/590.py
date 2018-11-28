'''
Created on Apr 11, 2014

@author: mandy
'''
import sys
numLinePerTest = 10

def magicTrick(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    numTests = int(lines[0])
    
    for i in xrange(numTests):
        currentRow = i*numLinePerTest+1
        firstRow = getChosenRowData(currentRow, lines)
        currentRow += int(0.5*numLinePerTest)
        secRow = getChosenRowData(currentRow, lines)
        output(i, firstRow, secRow)
        
        
def getChosenRowData(startRowID, lines):
    rowChoice = int(lines[startRowID])
    return lines[startRowID+rowChoice].strip('\n').split(' ')

def output(currentRow, firstRow, secRow):
    count = 0
    card = -1
    for f in firstRow:
        if f in secRow:
            count += 1
            card = f
            if count > 1:
                print 'Case #'+str(currentRow+1)+': Bad magician!'
                return
    if count == 0:
        print 'Case #'+str(currentRow+1)+': Volunteer cheated!'
    elif count == 1:
        print 'Case #'+str(currentRow+1)+': '+card
    return

def main():
    currentPath = sys.argv[0]
    currentPath = currentPath[:currentPath.rfind('/')]
    file = currentPath+'/A-small-attempt4.in'
    magicTrick(file)

if __name__ == '__main__':
    main()