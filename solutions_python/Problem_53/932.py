#!/usr/bin/env python

class PowerSource:
    def isGivingPower(self):
        return True

class Snapper:
    def __init__(self, id, input, on=False):
        self.id = id
        self.input = input
        self.on = on
        self.nextRoundOn = False
    
    def toggle(self):
        if self.on == True:
            self.nextRoundOn = False
        else:
            self.nextRoundOn = True

    def toggleIfHasPower(self):
        if self.input.isGivingPower():
            self.toggle()

    def isGivingPower(self):
        if self.input.isGivingPower() and self.on:
            return True
        return False
    
    def goToNextRound(self):
        self.on = self.nextRoundOn

class TestCase:
    def __init__(self, numOfSnappers, numOfSnaps):
        self.numOfSnappers = numOfSnappers
        self.numOfSnaps = numOfSnaps
        self.snappers = []
        self.lastSnap = None
        self.setUpSnappers()

    def run(self):
        for i in range(self.numOfSnaps):
            for j in self.snappers:
                j.toggleIfHasPower()
                #print str(j.on) + '  ',
            #print ''
            for j in self.snappers:
                j.goToNextRound()

    def setUpSnappers(self):
        oldSnap = PowerSource()
        for i in range(self.numOfSnappers):
            snap = Snapper(i+1, oldSnap)
            self.snappers.append(snap)
            oldSnap = snap
            if (i+1)==self.numOfSnappers:
                self.lastSnap = snap

    def isLightOn(self):
        return self.lastSnap.isGivingPower()

if __name__=='__main__':
    import sys
    inputFile = sys.argv[1]
    data = open(inputFile).read()
    numOfCases = int(data.splitlines()[0])
    outData = []
    for i in range(numOfCases):
        line = data.splitlines()[i+1]
        n, k = line.split(' ')
        case = TestCase(int(n), int(k))
        case.run()
        caseData = 'Case #' + str(i+1)  + ': '
        if case.isLightOn():
            caseData += 'ON'
        else:
            caseData += 'OFF'
        outData.append(caseData)

    outFile = open(inputFile.split('.')[0]+'.out', 'w')
    outFile.write('\n'.join(outData))
