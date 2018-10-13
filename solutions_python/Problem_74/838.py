class Robot:
    def __init__(self, asteps):
        self.steps = asteps
        self.si = 0
        self.counter = 0
        self.wait = False
        self.position = 1
        self.end = False

    def setFriend(self, rb):
        self.friend = rb

    def iterate(self):
        self.counter = self.counter + 1
        if(self.end):
            self.wait = False
            return
        if(self.si >= len(self.steps)):
            self.wait = False
            self.end = True
            return 
        if(self.wait == True):
            dif = self.steps[self.si] - self.position
            if(dif <> 0):
                signo = dif/abs(dif)
                self.position = self.position + signo    
        else:
            if(self.si == len(self.steps)-1):
                dif = self.steps[self.si] - self.position
                if(dif <> 0):
                    signo = dif/abs(dif)
                    self.position = self.position + signo
                else:
                    self.counter = self.counter + 1
                    self.wait = False
                    self.end = True
            else:
                dif = self.steps[self.si] - self.position
                if(dif <> 0):
                    signo = dif/abs(dif)
                    self.position = self.position + signo
                else:
                    self.wait = True
                    self.si = self.si + 1
                    self.counter = self.counter + 1
            
    def __str__(self):
        strr = str(self.steps) + ", " + str(self.si) + ", " + str(self.wait) + ", pos=" + str( self.position)
        return strr

def load(line):
    chars = line.split()
    N = int(chars[0])
    i = 1
    stepO = []
    stepB = []
    steps = []

    while(i<=N):
        steps.append(chars[i*2-1])
        if(chars[i*2-1] == "O"):
            stepO.append(int(chars[i*2]))
        else:
            stepB.append(int(chars[i*2]))
        i = i + 1
    return steps, stepO, stepB

def avance( steps, pos):
    if(len(steps)>0):
        dif = steps[0] - pos
        if(dif <> 0):
            signo = dif/abs(dif)
            pos = pos + signo
    return steps, pos

def test(line):
    steps, stepO, stepB = load(line)
    counter = 0
    posO = 1
    posB = 1
    for i in steps:
        paso = False
        while(paso == False):
            if(i == "O"):
                if(posO == stepO[0]):
                    counter = counter + 1
                    stepO = stepO[1:]
                    stepB,posB = avance(stepB,posB)
                    paso = True
                else:
                    counter = counter + 1
                    stepO,posO = avance(stepO,posO)
                    stepB,posB = avance(stepB,posB)                
            else:
                if(posB == stepB[0]):
                    counter = counter + 1
                    stepB = stepB[1:]
                    stepO,posO = avance(stepO,posO)
                    paso = True
                else:
                    counter = counter + 1
                    stepB,posB = avance(stepB,posB)
                    stepO,posO = avance(stepO,posO)
            
    return counter
            
def solver(name):
    arch = file(name, "r")
    output = file("ouput-large.txt", "w")
    outstr = ""
    N = int(arch.readline())
    lines  =arch.readlines()
    for i in range(N):
        line = lines[i]
        outstr = outstr + "Case #" + str(i + 1) + ": " + str(test(line)) + "\n"

    output.write(outstr)
    output.close()
    arch.close()
