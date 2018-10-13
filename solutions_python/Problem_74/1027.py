#!/usr/bin/env python
'''
Bot Trust
'''

import sys

def read_input(fname):
    cases = []
    with open(fname) as f:
        case_num = int(f.next().strip())
        for line in f:
            cases.append(Case(line.strip()))
    return cases
    
class Case(object):
    def __init__(self,str):
        cols = str.split()
        self.buttons = int(cols[0])
        self.presses = []
        
        o_targets = []
        b_targets = []
        for bot,button in zip(cols[1::2],[int(x) for x in cols[2::2]]):
            self.presses.append((bot,button))
            if bot == 'O':
                o_targets.append(button)
            else:
                b_targets.append(button)
        
        self.blue = Bot('Blue', b_targets)
        self.orange = Bot('Orange', o_targets)

    def solve(self):
        _log('---------------------------')
        _log(str(self.presses))
        t = 0
        while self.presses:
            t += 1
            next_press = '%s %s' % self.presses[0]
            
            if self.presses[0][0] == 'O' and self.orange.can_push:
                self.orange.push()
                self.blue.move()
                if len(self.presses) > 1:
                    next_press = '%s %s' % self.presses[1]
                else:
                    next_press = '*****'
                self.presses = self.presses[1:]
            elif self.presses[0][0] == 'B' and self.blue.can_push:
                self.blue.push()
                self.orange.move()
                if len(self.presses) > 1:
                    next_press = '%s %s' % self.presses[1]
                else:
                    next_press = '*****'
                self.presses = self.presses[1:]
            else:
                self.blue.move()
                self.orange.move()
            
            _log('%4s | %20s | %20s | Next push: %s' % (t,self.orange.action,self.blue.action, next_press))

        return t

def _log(s):
    return
    sys.stderr.write('%s\n' % s)
            

class Bot(object):
    def __init__(self,name, targets):
        self.name = name
        self.pos = 1
        self.targets = targets
        self.action = 'Do nothing'
        self.can_push = False

        if self.targets and self.pos == self.targets[0]:
            self.can_push = True

    def move(self):
        if not self.targets:
            self.action = 'Do nothing'
            return
   
        if self.pos == self.targets[0]:
            self.action='Staying at #%s' % self.pos
        elif self.pos < self.targets[0]:
            self.pos += 1
            self.action = 'Moving to #%s [%s]' % (self.pos, self.targets[0])
        elif self.pos > self.targets[0]:
            self.pos -= 1
            self.action = 'Moving to #%s [%s]' % (self.pos, self.targets[0])

        if self.pos == self.targets[0]:
            self.can_push = True

    def push(self):
        if self.can_push:
            self.action = 'Pushing button #%s' % self.pos
            self.targets = self.targets[1:]
            
            if self.targets and self.pos == self.targets[0]:
                self.can_push = True
            else:
                self.can_push = False
    

if __name__ == '__main__':
    cases = read_input(sys.argv[1])
    
    for num,case in enumerate(cases):
        t = case.solve()
        print 'Case #%s: %s' % (num+1,t)
        # sys.stderr.write('Case #%s: %s\n' % (num+1,t))
        # sys.stdin.readline()