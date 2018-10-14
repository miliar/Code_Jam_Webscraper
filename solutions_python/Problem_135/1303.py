



def start():
    f = file("Solution1.in")
    numberOfCases = int(f.readline().rstrip())
    for trial in xrange(0,numberOfCases): 
        doesTheRowTheContestantPickedContainSomeValues = False
        magicianSucks = False
        grid = []
        
        firstIndex = int(f.readline().rstrip()) - 1
        
        for x in xrange(0,4):
            grid.append(f.readline().rstrip().split())

        firstSelectedRow = grid[firstIndex]
        secondSelectedRow = []
        
        secondIndex = int(f.readline().rstrip()) - 1
        
        movedGrid = []
        for x in xrange(0,4):
            movedGrid.append(f.readline().rstrip().split())

        columnFound = False
        columnIndex = 0
        
        for col_index, item in enumerate(movedGrid[secondIndex]):
            doesTheRowTheContestantPickedContainSomeValues |= item in firstSelectedRow
            if doesTheRowTheContestantPickedContainSomeValues:
                columnIndex = col_index
                break
                
        for row in movedGrid:
            for value in row:
                if value in firstSelectedRow:
                    secondSelectedRow.append(value)
                    

        counter = 1
        for row in movedGrid:
            tempCounter = 0
            for value in row:
                if value in secondSelectedRow:
                    tempCounter = tempCounter + 1
            if tempCounter > counter: counter = tempCounter
        
        
        if counter > 1:
            for item in movedGrid[secondIndex]:
                if item in secondSelectedRow: counter = counter - 1

        selection = 0

        if counter == 1: 
            for item in movedGrid[secondIndex]:
                if item in secondSelectedRow: selection = item 

        if not doesTheRowTheContestantPickedContainSomeValues:
            print "Case #%i: Volunteer cheated!" % (trial + 1)
        else:
            if counter != 1: print "Case #%i: Bad magician!" % (trial + 1)
            else: print "Case #%i: %s" % (trial + 1,selection)
        
if __name__ == "__main__":
    start()