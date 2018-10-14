#!/usr/bin/env python

import sys


class robot(object):
    def __init__(self, color, case = []):
        self.case = case
        self.color = color
        self.pos = 1
        self.index = 0

    def set_case(self, case):
        for x in case:
            self.case.append(x) # hack to have shared list for all robots

    def finished(self):
        return self.case == []

    def need_to_play_first(self):
        return self.case[0][0] == self.color

    def doAction(self, permission_to_switch=False):
        if( self.case != []):
            next_target = None
            for c in self.case:
                if c[0]==self.color:
                    next_target = c 
                    break
            if next_target is not None:
                next_pos = next_target[1]
                if next_pos == self.pos:
                    if next_target == self.case[0] and permission_to_switch:
                        # print self.color, "depop", next_target
                        self.case.pop(0)
                        return False # return True if we switched 
                    else:
                        # print self.color, "stays in position", next_pos
                        pass
                elif next_pos > self.pos:
                    self.pos += 1
                    # print self.color, "goes to", self.pos
                else:
                    self.pos -= 1
                    # print self.color, "goes to", self.pos
        return True 



def solve(case):
    both = []
    next_switch = []
    case_split = case.split(" ")
    num_case = int(case_split.pop(0))
    for x in case_split:
        if x == 'O':
            next_switch = ['O']
        elif x == 'B':
            next_switch = ['B']
        else:
            next_switch.append(int(x))
            both.append(next_switch)
    assert( len(both)==num_case )
   
    # print "solving case:", both
    orange = robot('O')
    blue = robot('B')
    
    blue.set_case(both)
       
    t = 0
    while not (orange.finished() and blue.finished()):
        #print "t=",t
        if orange.need_to_play_first():
            blue.doAction(orange.doAction(True))
        else:
            orange.doAction(blue.doAction(True))
        t += 1
    return t 

def parse_args():
    f = open(sys.argv[1]) 
    n = int(f.readline().strip())
   
    for i in xrange(1,n+1):
        case = f.readline().strip()
        print "Case #" + str(i)+ ":", solve(case)

parse_args()
