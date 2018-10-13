'''
Created on May 7, 2011

@author: jagadeesh
'''

from sys import stdin

class Robot:
    BLUE = 'B'
    ORANGE = 'O'

    UNKNOWN_TARGET = -1
    
    def __init__(self, name):
        self.name = name
        self.targets = []
        self.position = 1
        self.target = Robot.UNKNOWN_TARGET
        self.factor = 1
    
    def __repr__(self):
        return "Robot(%s, p: %s, t: %s): %s %s" % (self.name, self.position, self.target, self.targets, self.factor)
    
    def __str__(self):
        return "Robot(%s, p: %s, t: %s): %s %s" % (self.name, self.position, self.target, self.targets, self.factor)
    
    def add(self, cmd):
        self.targets.append(cmd)
    
    def decideTarget(self):
        if len(self.targets) > 0:
            self.target = self.targets[0]
            del self.targets[0]
            if self.target < self.position:
                self.factor = -1
            else:
                self.factor = 1
        else:
            self.target = Robot.UNKNOWN_TARGET

        
    def execute(self, name):
        if self.target == Robot.UNKNOWN_TARGET:
            return True
        
        if self.name != name:
            self._move()
            return True
        
        if self.target == self.position:
            self.decideTarget()
            return True
        
        self._move()
        return False
        

    def _move(self):
        if self.target == self.position: return
        
        self.position = self.position + self.factor
        


        
    
class Problem:
    
    def __init__(self):
        self.T = 0
        self.commands = []
        self.blue = Robot(Robot.BLUE)
        self.orange = Robot(Robot.ORANGE)
        self.case = 0
        
    
    def _readT(self):
        self.T = int(stdin.readline())
    
    
    def _readSequence(self):
        self.blue = Robot(Robot.BLUE)
        self.orange = Robot(Robot.ORANGE)
        self.commands = []

        line = stdin.readline()
#        print "line: %s" % line
        
        parts = line.split()
        del parts[0]
        
        index = 0
        for _ in range(len(parts)/2):
            self.commands.append(parts[index])
            seq = int(parts[index+1])
            if parts[index] == Robot.BLUE:
                self.blue.add(seq)
            else:
                self.orange.add(seq)
            index += 2
        
        
    def __call__(self):
        
        self._readT()
        self.case = 0
        for _ in range(self.T):
            self._readSequence()
            self.case += 1
            yield self.case
    
    
    
    def solve(self):
#        print "Case #%s: " % self.case
#        print "commands: %s" % self.commands
#        print self.blue
#        print self.orange
        
        self.blue.decideTarget()
        self.orange.decideTarget()
        time = 0
        for cmd in self.commands:
            while True:
#                print "Time: %s %s" % (time, cmd)
                r1 = self.blue.execute(cmd)
                r2 = self.orange.execute(cmd)
#                print self.blue
#                print self.orange
                if r1 and r2 : 
                    time += 1
                    break
                time += 1

        print "Case #%s: %s" % (self.case, time)
            

    
if __name__ == "__main__":
    
    problem = Problem()
    for case in problem():
        problem.solve()
    
