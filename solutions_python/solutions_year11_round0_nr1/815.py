'''
Created on May 7, 2011

@author: michael
'''
def processCaseStr(charArray):
    case = []
    for i in range(0,len(charArray),2):
        case.append([charArray[i],int(charArray[i+1])])
    return case

def readInputFile(fname):
    inputFile = open(fname,'r')
    numOfCases = int(inputFile.readline().strip())
    cases = []
    for i in range(numOfCases):
        line = inputFile.readline().strip()
        caseStr = line.split(' ')
        caseStr.pop(0)
        cases.append(processCaseStr(caseStr))
    return cases

def writeOutputFile(fname,times):
    outputFile = open(fname,'w')
    for i,time in enumerate(times):
        if i != len(times)-1:
            outputFile.write( 'Case #%i: %i\n' % (i+1,time) )
        else:
            outputFile.write( 'Case #%i: %i' % (i+1,time) )
    outputFile.close()
    
class robot(object):
    
    def __init__(self,name,buttonOrder):
        self.curPos = 1
        self.name = name
        self.buttonOrder = buttonOrder
    def atNextButton(self):
        if self.buttonOrder[0] == self.curPos:
            return True
        else:
            return False
    def ordersComplete(self):
        if len(self.buttonOrder) == 0:
            return True
        else:
            return False
    def pushButton(self):
        #print '%s pushed button %i' % (self.name,self.buttonOrder[0])
        self.buttonOrder.pop(0)
    def moveTowardsNextButton(self):
        if not self.atNextButton():
            if self.buttonOrder[0] > self.curPos:
                self.curPos += 1
                #print '%s moved to %s' % (self.name,self.curPos)
                return
            else :
                self.curPos -= 1
                #print '%s moved to %s' % (self.name,self.curPos)
                return
        else:
            #print '%s waiting at %s' % (self.name, self.curPos)
            return
cases = readInputFile('A-large.in')
#cases = [ [ ['O',2], ['B', 1], ['B', 2], ['O', 4] ] ]

timeTakenArray = []
for case in cases:
    print 'Starting New Case'
    
    orangeButtonOrder = []
    blueButtonOrder = []
    for command in case:
        if command[0] == 'O':
            orangeButtonOrder.append(command[1])
        elif command[0] == 'B':
            blueButtonOrder.append(command[1])
    orangeRobot = robot('orange',orangeButtonOrder)
    blueRobot = robot('blue',blueButtonOrder)
    
    finished = False
    timeTaken = 0
    while not finished:
        if len(case) == 0:
            finished = True
            break
        timeTaken += 1
        nextCommand = case[0]
        if nextCommand[0] == 'O' and not orangeRobot.ordersComplete():
            if blueRobot.ordersComplete() == False:
                blueRobot.moveTowardsNextButton()
                
            if orangeRobot.atNextButton():
                orangeRobot.pushButton()
                case.pop(0)
            else:
                orangeRobot.moveTowardsNextButton()
        elif nextCommand[0] == 'B' and not blueRobot.ordersComplete():
            if orangeRobot.ordersComplete() == False:
                orangeRobot.moveTowardsNextButton()
                
            if blueRobot.atNextButton():
                blueRobot.pushButton()
                case.pop(0)
            else:
                blueRobot.moveTowardsNextButton()
    timeTakenArray.append(timeTaken)
    
writeOutputFile('A-large.out',timeTakenArray)