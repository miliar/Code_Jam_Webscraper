
class Problem(object):
    def __init__(self):
        self.numGoals = None
        self.numAchievedGoals = 0
        self.robots = {"O": Robot(), "B": Robot()}
        Robot.setProblem(self)
        
    def loadProblem(self, line):
        split = line.split(" ")
        numGoals = int(split[0])
        assert len(split) == 2 * numGoals + 1
        self.numGoals = numGoals
        for i in range(numGoals):
            robotName = split[i * 2 + 1]
            assert robotName == "O" or robotName == "B"
            destination = int(split[i * 2 + 2])
            
            self.robots[robotName].goals.append((destination, i))
#            print("Goal#%d: Move %s to %d" % (i, robotName, destination))
            
#        self.robots["O"].dump()
#        self.robots["B"].dump()

    def solve(self):
        time = 0
        while self.numAchievedGoals < self.numGoals:
            anotherGoalAchieved = False
            actions = {}
            for (name, robot) in self.robots.items():
                (action, achieved) = self.robots[name].work()
                if achieved:
                    assert not anotherGoalAchieved  # only one goal at one turn
                    anotherGoalAchieved = True
                actions[name] = action
            if anotherGoalAchieved:
                self.numAchievedGoals +=1
#            print "%30s %30s" % (actions["O"], actions["B"])
            time += 1
#        print "time = %d" % time 
        return time
    
    
class Robot(object):
    problem = None
    def __init__(self):
        self.pos = 1
        self.goals = []
        # [(destination1, seq1), (destination2, seq2), ...]
        # Should reach destination_i only after seq_i
        self.goalPointer = 0
    
    def dump(self):
        print("Pos: %d" % self.pos)
        print("Goals: %s" % str(self.goals))
        print("Num. achieved goals: %d" % self.problem.numAchievedGoals)
    
    @classmethod
    def setProblem(cls, problem):
        cls.problem = problem   # pointer to the (shared) problem
    
    def work(self):
        anotherGoalAchieved = False
        if self.goalPointer >= len(self.goals):
            action = "Stay at button %d" % self.pos
            return (action, anotherGoalAchieved)
        (destination, seq) = self.goals[self.goalPointer]
        if self.pos > destination:
            self.pos -= 1
            action = "Move to button %d" % self.pos
        elif self.pos < destination:
            self.pos += 1
            action = "Move to button %d" % self.pos
        else:
            if self.problem.numAchievedGoals >= seq:
                action = "Push button %d" % destination
                anotherGoalAchieved = True
                self.goalPointer += 1
            else:
                action = "Stay at button %d" % self.pos
        return (action, anotherGoalAchieved)
    
def main():
    file = open("e:\\temp\\A-small-attempt0.in", "r")
    numProblems = int(file.readline().strip())
    for i in range(numProblems):
        p = Problem()
        p.loadProblem(file.readline().strip())
        print "Case #%d: %d" % (i + 1, p.solve())
    
if __name__ == "__main__":
    main()
    
    

