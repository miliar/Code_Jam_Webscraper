import tokenize

class Robot:
    nextDestinies = []
    pushed = False

    def __init__(self, name):
        self.name = name
        self.pos = 1
        self.destinations = []

    def addDestination(self, dest):
#        print "addDestination : " + self.name + " :" + str(dest)
        self.destinations.append(dest)

    def pushButton(self):
        assert self.pos == self.destinations[0]
        if Robot.nextDestinies[0] != self.name:
            return
#        print "pushButton : " + self.name + " :" + str(self.pos)
        self.destinations.pop(0)
        Robot.pushed = True
        del Robot.nextDestinies[0]

    def proceed(self):
        if self.pos > self.destinations[0]:
            self.pos -= 1
        else:
            self.pos += 1
#        print "Move : " + self.name + " :" + str(self.pos)

    def isDestination(self):
#        print "isDestination : " + self.name + " : dest=" + str(self.destinations[0]) + " pos= " + str(self.pos)
        return (not self.isGoal()) and self.pos == self.destinations[0]

    def isGoal(self):
#        print("isGoal " + str(len(self.destinations) == 0))
        return len(self.destinations) == 0

    def dump(self):
        print "###dump###"
        print self.name
        print self.destinations
        print self.pos
        print "##########"

f = open("A-small-attempt0.in")

lineNum = int(f.readline())
testCases = []
for line in f.readlines():
    testCases.append(line[2:].strip().split(" "))

testNum = 1
for testCase in testCases:
#    print testCase

    robotO = Robot("O")
    robotB = Robot("B")
    destinies = ""

    for i in range(0, len(testCase), 2):
        Robot.nextDestinies.append(testCase[i])
        if testCase[i] == "O":
            robotO.addDestination(int(testCase[i+1]))
        elif testCase[i] == "B":
            robotB.addDestination(int(testCase[i+1]))
        else:
            assert False

#    robotO.dump()
#    robotB.dump()
#    print destinies

    cnt = 0
    while robotO.isGoal() == False or robotB.isGoal() == False:
        cnt += 1
        Robot.pushed = False
#        print "#### turn : " + str(cnt) + " ####"
        if robotO.isDestination():
            robotO.pushButton()
        elif not robotO.isGoal():
            robotO.proceed()

        if robotB.isDestination():
            if not Robot.pushed:
                robotB.pushButton()
        elif not robotB.isGoal():
            robotB.proceed()

    print "Case #"+str(testNum)+": " + str(cnt)
    testNum += 1

f.close()
