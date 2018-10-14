from setuptools.command.bdist_egg import analyze_egg
                    
class Robot:
    def __init__(self, case, color):
        self.pushes = []
        self.color = color
        while len(case) > 0:
            if case.pop(0)==color:
                self.pushes.append((int)(case.pop(0)))
            else:
                case.pop(0)
        self.currPos = 1
    
    def shouldMove(self):
        if len(self.pushes)>0:
            return self.currPos!=self.pushes[0]
        return False
    
    def isAtPush(self):
        return self.pushes[0]==self.currPos
    
    def push(self):
        self.pushes.pop(0)
    
    def nextPush(self):
        return self.pushes[0]
    
    def move(self):
        if self.pushes[0]>self.currPos:
            self.currPos += 1
        else:
            self.currPos -= 1
            
    
    def getCurrPos(self):
        return self.currPos
    
    def __str__(self):
        return self.color

class Case:    
    def analyze(self, file):
        T = file.readline()
        for i,case in enumerate(file):
            yield "Case #%d: %d" % (i+1,self.analyze_case(case))        
    def analyze_case(self,case):
        vals = case.split(" ")
        nrOfPushes = vals.pop(0)
        robots = {"O":Robot([a for a in vals],"O"),"B":Robot([b for b in vals],"B")}
        pushList = [color for i,color in enumerate(vals) if i%2==0]
        completed = False
        curr = pushList.pop(0)
        currRobot = robots.get(curr)
        counter = 0
        while not completed and currRobot.getCurrPos()<101:
            other = "O" if curr == "B" else "B"
            currRobot = robots.get(curr)
            otherRobot = robots.get(other)
            if currRobot.isAtPush():
                currRobot.push()
                if len(pushList)>0:
                    curr = pushList.pop(0)
                else:
                    completed = True
            else:
                currRobot.move()
            if otherRobot.shouldMove():
                otherRobot.move()
            counter += 1
        return counter

b = open("A-large.in")
a = Case()
for i in a.analyze(b):
    print i