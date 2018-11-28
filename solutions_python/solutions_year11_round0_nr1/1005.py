#!/usr/bin/python

import sys
from pprint import pprint
from collections import deque

TAB = '   '

class Robot:
    def __init__(self, name, route, debug = False):
        self.name = name
        self.route = route
        self.N = len(self.route)
        self.ptr = -1
        self.pos = 1
        self.dest = -1
        self.canPush = False
        self.debug = debug

    def destValid(self):
        return (self.dest != -1)
        
    def updateDestination(self):
        dest = -1  # invalid destination
        ptr = 1000 # maximum number
        # start searchig from ptr+1
        for b in range(self.ptr+1, self.N):
            if self.route[b][0] == self.name[0]:
                ptr = b
                dest = self.route[b][1]
                break
        self.dest = dest
        self.ptr = ptr
        self.canPush = False
        if self.debug:
            print TAB, self.name, 'has a new destination', self.dest

    def act(self):
        if not self.destValid():
            if self.debug:
                print TAB, self.name, 'has no valid destination'
            return
        if self.debug:
            print TAB, self.name, 'has to walk from', self.pos, 'to', self.dest
        diff = self.dest - self.pos
        if diff > 0:
            self.moveFwd()
        elif diff < 0:
            self.moveBkw()
        elif diff == 0:
            self.pushBtn()
    
    def moveFwd(self):
        if self.debug:
            print TAB, self.name, 'moved forward from', self.pos, 'to', self.pos+1
        self.pos = self.pos + 1
        
    def moveBkw(self):
        if self.debug:
            print TAB, self.name, 'moved backward from', self.pos, 'to', self.pos-1
        self.pos = self.pos - 1
    
    def pushBtn(self):
        if self.canPush:
            if self.debug:
                print TAB, self.name, 'pushed #### button', self.pos, '###'
            self.updateDestination()
        else:
            if self.debug:
                print TAB, self.name, 'cannot yet push button', self.pos, ', standing by...'
        
def solveCase(route, debug = False):
    if debug or True:
        print 'Solving route: ',;   pprint(route)
    N = len(route)
    # create the robots
    b = Robot("Blue", route, debug)
    o = Robot("Orng", route, debug)
    
    # initialize robots
    b.updateDestination()
    o.updateDestination()
    time = 0

    while (1):
        ptr = min(b.ptr, o.ptr)
        if debug:
            print 'Time =', time, 'ptr =', ptr, 'b.ptr =', b.ptr, 'o.ptr =', o.ptr
        if not o.destValid() and not b.destValid():
            break
        # check if pushing the button is allowed        
        if b.destValid() and ptr == b.ptr:
            b.canPush = True
            if debug:
                print TAB, 'Next push by', b.name
        elif o.destValid() and ptr == o.ptr:
            o.canPush = True
            if debug:
                print TAB, 'Next push by', o.name
        # manipulate the robots
        b.act()
        o.act()
        # increment the time
        time = time + 1
#        if (time > 200):
#            break

    return time


def main(debug = False):
    if len(sys.argv) < 2:
        print 'no input file given!'
        return
        assert False
        
    fin = open(sys.argv[1])

    T = fin.readline() 
    T = int(T)


    result = list()
    for c in range(1, T+1):
        case = fin.readline().split()
        N = int(case[0])
        case = case[1:]
        route = deque()        
        for b in range(0, N):
            route.append( (case[2*b], int(case[2*b+1])) )
        time = solveCase(route, debug)
        result.append(time) 
    fin.close()

    fout = open('out.txt', 'w')
    print 'Results'
    for c in range(1, T+1):
        line = 'Case #%d: %d' % (c, result[c-1])
        print line
        fout.write(line)
        fout.write('\n')
    fout.close()

if __name__ == '__main__':
#    debug = True
    debug = False
    main(debug)
    
