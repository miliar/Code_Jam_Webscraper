'''
Created on May 7, 2011

@author: Guy
'''

class Robot:
    def __init__(self,targets,name):
        self.loc = 1
        self.targets=targets
        self.numTargets=len(targets)
        self.nextTarget = self.getTarget()
        self.name = name
    def getTarget(self):
        if len(self.targets)>0: return self.targets.pop(0)
        return None
    def onTarget(self):
        if self.nextTarget==self.loc: return True
        return False
    def makeMove(self):
        if self.loc<self.nextTarget:
            self.loc+=1
        if self.loc>self.nextTarget:
            self.loc-=1
    
        


def processLine(line):
    runOrder = []
    blueArr = []
    orangeArr = []
    s = line.split()
    N = int(s[0]) #number of bulbs to press
    for i in xrange(N):
        nextBot = s[2*i+1]
        runOrder.append(nextBot)
        if nextBot=='O':
            orangeArr.append(int(s[2*i+2]))
        elif nextBot=='B':
            blueArr.append(int(s[2*i+2]))
        else:
            print 'Color error!'
    return [runOrder, blueArr, orangeArr]


#return currentBot,otherBot
def getBots(c,B,O):
    if c=='B': return [B,O]
    elif c=='O': return [O,B]
    else: return None

def doRun(runOrder,B,O,fo,caseNum):
    numRounds = 0
    [currBot,otherBot] = getBots(runOrder.pop(0),B,O)
    currBot.target = currBot.getTarget
    otherBot.target = otherBot.getTarget
    while True:
#        print ('Round number: ' + str(numRounds) + 'Current bot: ' + currBot.name
#           + ' is at ' +str(currBot.loc) +', other bot('+otherBot.name+') is at ' 
#           + str(otherBot.loc))
        if B.target is None and O.target is None: break
        numRounds+=1
      
        otherBot.makeMove() #moves either way
        if currBot.onTarget() == False:
            currBot.makeMove()
            continue
        #otherwise - press the button - select the next runner
        currBot.nextTarget = currBot.getTarget()
        if len(runOrder)==0: break
        [currBot,otherBot] = getBots(runOrder.pop(0),B,O)
    resStr = 'Case #'+str(caseNum)+': ' + str(numRounds)
    print resStr        
    fo.write(resStr+'\n')

def processInput(inFileName,outFileName):
    f = open(inFileName)
    fo = open(outFileName,'w')
    numLines = int(f.readline().rstrip())
    for i in xrange(numLines):
        line = f.readline().rstrip()
        [runOrder,blueArr,orangeArr] = processLine(line)
        B = Robot(blueArr,'Blue')
        O = Robot(orangeArr,'Orange')
        doRun(runOrder,B,O,fo,i+1)
        
processInput('A-large.in', 'botOutLarge.txt')