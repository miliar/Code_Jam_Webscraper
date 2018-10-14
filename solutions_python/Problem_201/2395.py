
class Stall:
    def __init__(self, index, ocuppied, Lindex, Rindex):
        self.index = index
        self.ocuppied = ocuppied
        self.Lindex = Lindex
        self.L = self.index - self.Lindex - 1
        self.Rindex = Rindex
        self.R = self.Rindex - self.index - 1

    def update(self, stall):
        if self.index < stall.index:
            self.Rindex = stall.index
            self.R = self.Rindex - self.index - 1
        elif self.index > stall.index:
            self.Lindex = stall.index
            self.L = self.index - self.Lindex - 1
        else:
            self.ocuppied = True
            self.L = -1
            self.R = -1

def debug(stalls):
    print 'O',
    for stall in stalls:
        if stall.ocuppied:
            print 'O',
        else:
            print '.',
    print 'O',
    print

def selectNextStall(stalls):
    selectedStall = stalls[0]
    for stall in stalls[1:]:
        if min(stall.L, stall.R) > min(selectedStall.L, selectedStall.R):
            selectedStall = stall
        elif min(stall.L, stall.R) == min(selectedStall.L, selectedStall.R):
            if max(stall.L, stall.R) > max(selectedStall.L, selectedStall.R):
                selectedStall = stall
    return selectedStall

def update(stalls, selectedStall):
    for stall in stalls[selectedStall.Lindex + 1:selectedStall.Rindex - 1 + 1]:
        stall.update(selectedStall)

class TestCase:
    def __init__(self, caseIndex):
        self.caseIndex = caseIndex

    def parseInput(self):
        self.N, self.K = raw_input().split()
        self.N = int(self.N)
        self.K = int(self.K)

        self.maxS = 0
        self.minS = 0

    def run(self):
        self.stalls = []
        for index in range(0, self.N):
            self.stalls.append(Stall(index, False, -1, self.N))

        for selectIndex in range(0, self.K):
            nextStall = selectNextStall(self.stalls)
            self.maxS = max(nextStall.L, nextStall.R)
            self.minS = min(nextStall.L, nextStall.R)
            update(self.stalls, nextStall)

    def generateOutput(self):
        print "Case #%d: %d %d" % (self.caseIndex, self.maxS, self.minS)

for caseIndex in range(1, int(raw_input()) + 1):
    testCase = TestCase(caseIndex)
    testCase.parseInput()
    testCase.run()
    testCase.generateOutput()
