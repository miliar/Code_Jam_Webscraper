#!/usr/bin/python2.6
import re

class Robot():
    def __init__(self, symbol):
        self.symbol = symbol
        self.position = 1
        self.instructions = []
    def queue(self, instruction):
        self.instructions.append(instruction)
    def move(self):
        if len(self.instructions) == 0:
            return
        if self.position > self.instructions[0]:
            self.position -= 1
        elif self.position < self.instructions[0]:
            self.position += 1
    def push(self):
        del self.instructions[0]
    def isAtButton(self):
        return len(self.instructions) > 0 and self.position == self.instructions[0]

def solve(instructionCount, instructionSequence):
    robotSelection = re.findall("(\w+) \w+", instructionSequence)
    buttonIndex = re.findall("\w+ (\w+)", instructionSequence)
    instructions = zip(robotSelection, buttonIndex)
    seconds = 0
    blueRobot = Robot('B')
    orangeRobot = Robot('O')
    def select(robot):
        if robot == 'B':
            return blueRobot
        else:
            return orangeRobot
    currentBot = None
    for i, instruction in enumerate(instructions):
        previousBot = currentBot
        currentBot = select(instruction[0])
        currentBot.queue(int(instruction[1]))
        if currentBot != previousBot and previousBot != None:
            while len(previousBot.instructions) > 0:
                while not previousBot.isAtButton():
                    previousBot.move()
                    currentBot.move()
                    seconds += 1
                previousBot.push()
                currentBot.move()
                seconds += 1
        if i + 1 == instructionCount:
            while len(currentBot.instructions) > 0:
                while not currentBot.isAtButton():
                    currentBot.move()
                    seconds += 1
                currentBot.push()
                seconds += 1
    return seconds

if __name__ == "__main__":
    testCaseCount = input()
    caseIndex = 1
    outputs = []
    while caseIndex <= testCaseCount:
        data = raw_input()
        output = solve(int(re.findall('(\w+)', data)[0]), ' '.join(re.findall('(\w+)', data)[1:]))
        outputs.append((caseIndex, output))
        caseIndex += 1
    for output in outputs:
        print("Case #%i: %i" % output)
