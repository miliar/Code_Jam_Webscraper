import collections

def prob1():

    f = open('input.txt', 'r')
    s = f.read()
    
    rows = s.split('\n')
       
    curRow = 0;
    numProb = int(rows[0])
    curRow += 1

    
    for curProb in range(1, 1 +numProb):
        rowpick1 = int(rows[curRow])
        row1 = rows[curRow + rowpick1]
        rowpick2 = int(rows[curRow + 5])
        row2 = rows[curRow + 5 + rowpick2]
        repeats = [x for x, y in collections.Counter((row1.split(' ') + row2.split(' '))).items() if y > 1]
        if len(repeats) == 1:
            print "Case #" + str(curProb) + ": " + str(repeats[0])
        if len(repeats) > 1:
            print "Case #" + str(curProb) + ": Bad magician!"
        if len(repeats) == 0:
            print "Case #" + str(curProb) + ": Volunteer cheated!"
        curRow += 10
        
    


prob1();
