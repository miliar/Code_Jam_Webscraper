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
        


class State:
    def __init__(self, fcost, fcps, goal, currentFarms, timeToGetHere):
        self.fcost = float(fcost);
        self.fcps = float(fcps);
        self.goal = float(goal);
        self.currentFarms = int(currentFarms);
        self.timeToGetHere = float(timeToGetHere);
        
    def getTotalTimeToGoal(self):
        return self.goal /(self.fcps*self.currentFarms + 2.0) + self.timeToGetHere
        
    def getNextState(self):
        timeToNextFarm = self.fcost / (self.fcps*self.currentFarms + 2.0)
        return State(self.fcost, self.fcps, self.goal, self.currentFarms+1, self.timeToGetHere + timeToNextFarm)
        
    
    
    
def prob2():

    f = open('input2b.txt', 'r')
    s = f.read()
    rows = s.split('\n')

    numProb = int(rows[0])
    
    ncps= 2.0


    for curProb in range(1, 1 +numProb):
        fcost, fcps, goal = rows[curProb].split(' ')
        s1 = State(fcost, fcps, goal, 0.0, 0.0)
        t1 = s1.getTotalTimeToGoal()
        while (True) :
            s2 = s1.getNextState()
            t2 = s1.getTotalTimeToGoal()
            if(t1 < t2):
                break
            s1 = s2;
            t1 = t2;
        print "Case #" + str(curProb) + ": " + str(t1)

        


prob2();