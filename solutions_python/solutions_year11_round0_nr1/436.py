import sys

IS_DEBUG = False
def dprint(item):
    if IS_DEBUG:
        print item


R_IDLE, R_WALKING, R_W2P, R_PUSHING = range(4)

class Robot:
    def __init__(self, name, goalfeed):
        self.name = str(name)
        self.position = 1
        self.nextgoalposition = 0
        self.nextgoalnumber = 0
        self.state = R_IDLE
        self.buddy = 0
        self.hasjusthitgoal = False

        self.goalfeed = goalfeed
        self.getnewgoal()

    def getnewgoal(self):
        goal = self.goalfeed.getnextgoal()
        if goal == None:
            self.nextgoalposition = 0
            self.nextgoalnumber = 0
            dprint("    (Robot "+self.name+" GOT NEW GOAL: NO MORE GOALS")
        else:    
            self.nextgoalposition = goal[1]
            self.nextgoalnumber = goal[2]
            dprint("    (Robot "+self.name+" GOT NEW GOAL: "+str(self.nextgoalposition)+", order "+str(self.nextgoalnumber)+")")
        

    def tick1(self):
        self.hasmoved = False
        self.hasjusthitgoal = False
        
        dprint("  Tick1: "+self.name)

        # if no goal, grab a new goal - idle if we're out of goals
        if self.nextgoalposition == 0:
            self.state = R_IDLE
            dprint("    Robot "+self.name+": IDLE")
            self.hasmoved = True

        else:
            # walking case
            if self.nextgoalposition != self.position:
                self.state = R_WALKING
                dprint("    Robot "+self.name+": WALKING")
                self.hasmoved = True
                if self.nextgoalposition > self.position: self.position += 1
                else: self.position -= 1

    def tick2(self):
        dprint("  Tick2: "+self.name)
        if self.hasmoved == False:
            if (self.nextgoalnumber < self.buddy.nextgoalnumber or self.buddy.nextgoalnumber == 0):
                self.state = R_PUSHING
                dprint("    Robot "+self.name+": PUSHING")
                self.hasmoved = True
                self.hasjusthitgoal = True
            else:
                self.state = R_W2P
                dprint("    Robot "+self.name+": W2P")
                self.hasmoved = True

    def tick3(self):
        if self.hasjusthitgoal:
            self.getnewgoal()
            self.hasjusthitgoal = False
                
class GoalFeed:
    def __init__(self, instfeed):
        self.instfeed = instfeed
        self.pos = 0
        
    def getnextgoal(self):
        if self.pos == len(self.instfeed): return None
        else:
            self.pos += 1
            return self.instfeed[self.pos-1]


if __name__ == "__main__":

    # set up
    numtestcases = int(sys.stdin.readline().rstrip())
    instructions = []
    
    # read in instructions for each test case
    for i in range(numtestcases):
        isstring = True
        isfirstinstruction = True
        instructions.append([[],[]]) # blue, orange

        # process instruction lines
        instructionnumber = 1
        for instruction in sys.stdin.readline().rstrip().split(' '):
            if isfirstinstruction:
                isfirstinstruction = False
                continue
            if isstring:
                thisinstruction = [str(instruction)]
                isstring = False
            else:
                thisinstruction.append( int(instruction) )
                thisinstruction.append( int(instructionnumber) )

                if thisinstruction[0] == "B": instructions[i][0].append(thisinstruction)
                else: instructions[i][1].append(thisinstruction)

                isstring = True
                instructionnumber += 1


    # wake up robots
    casenum = 1
    for testcase in instructions:
        dprint("Test case "+str(casenum))
        goals_b = GoalFeed(testcase[0])
        goals_o = GoalFeed(testcase[1])
        
        b = Robot("B", goals_b)
        o = Robot("O", goals_o)
        b.buddy = o
        o.buddy = b

        b.tick1()
        o.tick1()
        b.tick2()
        o.tick2()
        b.tick3()
        o.tick3()

        timer = 0

        while (b.state != R_IDLE or o.state != R_IDLE):
            b.tick1()
            o.tick1()
            b.tick2()
            o.tick2()
            b.tick3()
            o.tick3()
            timer += 1
        
        dprint("\n")
        print "Case #"+str(casenum)+": "+str(timer)
        casenum += 1
        


