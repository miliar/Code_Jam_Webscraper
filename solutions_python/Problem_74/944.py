'''
Created on 08/05/2011

@author: Admin
'''

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)


ACTION = enum('UP', 'DOWN', 'PUSH', 'WAIT')

class ButtonStep:
    def __init__(self, robot, position):
        self.done = False
        self.robot = robot
        self.position = int(position)
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return "Robot {0} needs to press button {1}".format(self.robot, self.position)
    
    def push(self, testBot):
        if (testBot.position != self.position):
            self.msg("Can't be pushed by {0}, not at same position!".format(testBot))
        else:
            self.done = True
        return self.done
            
    def msg(self, msg):
        print "Button {0}: {1}".format(self.position, msg)
    
class TestBot:
    def __init__(self, robot):
        self.robot = robot
        self.position = 1
        self.buttons = []
    
    def adviseOf(self, botStep):
        if (botStep.robot == self.robot):
            self.buttons.append(botStep)
            
    def chooseAction(self):
        if len(self.buttons) == 0:
            return ACTION.WAIT
        
        if self.position == self.buttons[0].position:
            if self.buttons[0].prev == None or self.buttons[0].prev.done:
                return ACTION.PUSH
            else:
                return ACTION.WAIT
        elif self.position < self.buttons[0].position:
            return ACTION.UP
        elif self.position > self.buttons[0].position:
            return ACTION.DOWN
        else:
            self.msg("Don't know what action to take!")
    
    def executeAction(self, action):
        if action == ACTION.UP:
            self.position += 1
            if self.position > 100:
                self.msg("Went past end of course!")
        elif action == ACTION.DOWN:
            self.position -= 1
            if self.position < 1:
                self.msg("Went past start of course!")
        elif action == ACTION.PUSH:
            currButton = self.buttons[0];
            if currButton == None:
                self.msg("No current button to push!")
            if currButton.push(self):
                del self.buttons[0]
        elif action == ACTION.WAIT:
            pass
        else:
            self.msg("No action to execute!")
            
    def msg(self, msg):
        print "{0}: {1}".format(self.robot, msg)
        
    def __repr__(self):
        return "{0} (@{1})".format(self.robot, self.position)     

def runTest(testCaseInput):
    splitInput = testCaseInput.split()
    numButtons = int(splitInput.pop(0))
    print "Looks like we have {0} buttons to press".format(numButtons)
    allButtons = []
    testBots = [TestBot('O'), TestBot('B')]
    for i in range(0, len(splitInput), 2):
        currStep = ButtonStep(robot=splitInput[i], position=splitInput[i + 1])
        if len(allButtons) > 0:
            currStep.prev = allButtons[len(allButtons) - 1]
            currStep.prev.next = currStep
            
        allButtons.append(currStep)
        for bot in testBots:
            bot.adviseOf(currStep)
            
        print currStep
    
    seconds = 0
    while (len(allButtons) > 0):
        for bot in testBots:
            bot.nextAction = bot.chooseAction()
        for bot in testBots:
            print "{0} about to execute {1}".format(bot, bot.nextAction)
            bot.executeAction(bot.nextAction)
        removeFirst = False
        for i, step in enumerate(allButtons):
            if step.done and i == 0:
                removeFirst = True
            elif (step.done):
                print "ERROR! Step done out of order: '{0}'".format(step)
        if removeFirst:
            removed = allButtons.pop(0)
            print "Completed {0}".format(removed)
        seconds += 1
    
    return seconds

if __name__ == '__main__':
    fInput = open('input.txt')
    fOutput = open('output.txt', 'w')
    
    numCases = int(fInput.readline().strip());
    for num in range(1, numCases + 1):
        testCaseInput = fInput.readline().strip();
        print "Running test {0}/{2} on '{1}'".format(num, testCaseInput, numCases)
        result = runTest(testCaseInput)
        toWrite = "Case #{0}: {1}\n".format(num, result)
        print toWrite
        fOutput.write(toWrite)
        
    print "All done!"
