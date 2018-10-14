


class State:
    def __init__(self, presses):
        self.presses = presses
        self.index = 0
        self.stepsTaken = 0
        self.positions = [1, 1]
    
    def isDone(self):
        return self.index >= len(self.presses)

    def nextPress(self):
        return self.presses[self.index]

    def nextPressForRobot(self, robot):
        for i in range(self.index, len(self.presses)):
            (presser, pos) = self.presses[i]
            if presser == robot:
                return pos
        return None

    def step(self):
        (nextPresser, nextTarget) = self.nextPress()
        pressed = False
        if self.positions[nextPresser] == nextTarget:
            self.index += 1
            pressed = True
        for (robot, pos) in enumerate(self.positions):
            if robot == nextPresser and pressed:
                continue
            target = self.nextPressForRobot(robot)
            if pos < target:
                self.positions[robot] += 1
            elif pos > target:
                self.positions[robot] -= 1
        self.stepsTaken += 1
        
    def run(self):
        while not self.isDone():
            self.step()
        return self.stepsTaken

def getRobot(ch):
    if ch == 'O':
        return 0
    if ch == 'B':
        return 1

def main():
    testFile = open("test.txt")
    numTestCases = int(testFile.readline())
    for i in range(numTestCases):
        line = testFile.readline().split(' ')
        presses = []
        for j in range(int(line[0])):
            presses.append((getRobot(line[2*j + 1]), int(line[2*j + 2])))
        res = State(presses).run()
        print("Case #%d: %d" % (i + 1, res))

main()
        
