import re

root = r"C:/Python27/Mine/codejam/"

def solve(fname,outname = "A-small.out"):
    infile = open(root + fname,'rU')
    outfile = open(root + outname,'w')
    return solve_inner(infile,outfile)

def solve_inner(infile,outfile):
    casesline = infile.readline()
    cases = int(casesline)
    for case in xrange(1,cases + 1):
        instructionsline = infile.readline()
        instructionset = instructionsline.split(" ")
        numInstructions = int(instructionset[0])
        instructions = []
        for i in xrange(1,numInstructions + 1):
            instructions.append((instructionset[2*i - 1] == "O",int(instructionset[2*i])))
        if case > 1:
            outfile.write("\n")
        outfile.write("Case #%s: %s" % (case,processCase(instructions)))
    return True

def processCase(instructions):
    time = 0
    falseInstructions = [i[1] for i in reversed(instructions) if not i[0]]
    trueInstructions = [i[1] for i in reversed(instructions) if i[0]]
    order = [i[0] for i in reversed(instructions)]
    falseBot = Robot(falseInstructions)
    trueBot = Robot(trueInstructions)
    while len(order) > 0:
        which = order.pop()
        if which:
            bot = trueBot
            other = falseBot
        else:
            bot = falseBot
            other = trueBot
        dist = bot.goalDistance()
        bot.iterate(dist)
        other.iterate(dist + 1)
        bot.push()
        time += dist + 1
    return time

class Robot(object):
    def __init__(self,instructions):
        self._instructions = instructions
        self._position = 1
        self._newGoal()

    def goalDistance(self):
        if self._goal:
            return abs(self._goal - self._position)
        else:
            return 0

    def goalDirection(self):
        if self._goal:
            return cmp(self._goal - self._position,0)
        else:
            return 0

    def iterate(self,time):
        if self._goal:
            distance = self.goalDistance()
            if distance <= time:
                self._position = self._goal
            else:
                self._position += time*self.goalDirection()
            return min((distance,time))
        return 0

    def push(self):
        if self._position != self._goal:
            raise Exception("Must be at button position!")
        self._newGoal()

    def _newGoal(self):
        if self._hasInstructions():
            self._goal = self._instructions.pop()
        else:
            self._goal = 0

    def _hasInstructions(self):
        return len(self._instructions) > 0
