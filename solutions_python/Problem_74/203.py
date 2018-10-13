import sys, math, re

class Robot:
    def __init__(self, name, actions):
        self.name = name
        self.actions = actions
        self.location = 1
        self.desiredLocation = 0
        self.actionTime = 0
        self.stage=0
        self.findDesiredLocation()
        
    def step(self, stage):
        if not self.desiredLocation:
            return
        self.stage = stage
        if stage==self.actionTime and self.desiredLocation == self.location:
            # pressed the button and switched to further action
            self.stage += 1
            self.findDesiredLocation()
        elif self.desiredLocation > self.location:
            self.location += 1
        elif self.desiredLocation < self.location:
            self.location -= 1
    
    def findDesiredLocation(self):
        self.desiredLocation = 0
        self.actionTime = 0
        for i in xrange(self.stage, len(self.actions)):
            if self.actions[i]:
                self.actionTime = i
                self.desiredLocation = self.actions[i]
                break 
        

def main():
#    inFile = sys.__stdin__
#    outFile = sys.__stdout__
    inFile = open('A-large.in', 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
    T = int(inFile.readline())
    for t in xrange(1,T+1):
        op = []
        bp = []
        for m in re.finditer(r"(O|B) (\d+)", inFile.readline()):
            n = int(m.group(2))
            if m.group(1)=='O':
                op.append(n)
                bp.append(0)
            else:
                op.append(0)
                bp.append(n)
        o = Robot('O', op)
        b = Robot('B', bp)
        ret = 0
        stage = 0
        N = len(op)
        while True:
            if not o.desiredLocation and not b.desiredLocation:
                break
            ret += 1
            o.step(stage)
            b.step(stage)
            stage = max(o.stage, b.stage)
        outFile.write('Case #%d: %d\n' % (t, ret))

if __name__ == '__main__':
    main()
