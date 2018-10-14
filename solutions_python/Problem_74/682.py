import scipy as sp
import numpy as np
import sys

class Robot:
    def __init__(self, name, route):
        self.name = name
        self.route = route
        self.pos = 1
        if self.route and self.pos == self.route[0]:
            self.atpos = True
        else:
            self.atpos = False
    
    def move(self, nextbutton):
        print self.name, "Current route", self.route, "len:", len(self.route)
        if len(self.route) == 0:
            return 0
        
        if self.atpos:
            if nextbutton == (self.name, self.pos):
                print self.name, "pressing button", nextbutton
                dummy = self.route.pop(0)
                print self.name, "Route after pop:", self.route
                if self.route and self.pos == self.route[0]:
                    self.atpos = True
                else:
                    self.atpos = False
                return 1
            else:
                print self.name, "I'm waiting for button",nextbutton,"to be pressed"
                return 0
            
        dist = self.route[0] - self.pos
        if dist:
            self.pos += (dist / abs(dist))
            print self.name, "moving at pos", self.pos
            
            if self.pos == self.route[0]:
                print self.name, "I'm at pos", self.pos
                self.atpos = True
        
        return 0
            
    # def press(self, nextbutton):
        # if self.atpos:
        # else:
        #     self.move()
            
#end of class Robot


results = []

""" Read in input """
f = open("A-large.in")
data = f.readlines()
f.close()

data = map(str.strip, data)

# number of test cases
testcases = int(data[0])

for testcase in data[1:]:
    # extract sequence
    ar = testcase.strip().split(' ')
    
    # number of elements in sequence
    elnum = int(ar[0])
    
    x = ar[1::2]
    y = ar[2::2]
    y = map(int, y)

    route = zip(x, y)
    print route
    
    
    Oroute = []
    Broute = []
    for r in route:
        if r[0] == "O":
            Oroute.append(r[1])
        if r[0] == "B":
            Broute.append(r[1])
    print Oroute
    print Broute
    
    robotO = Robot('O', Oroute)
    robotB = Robot('B', Broute)
    
    time = 0
    pressed = 0
    for r in route:
        print r
        while True:
            time += 1
            print "Time:", time
            retO = robotO.move(r) 
            retB = robotB.move(r)
            
            print "Robot O resp:", retO, "Robot B resp:", retB
            if retO or retB:
                break
            
            # if time == 1000:
            #     print "BAILING OUT"
            #     sys.exit()
        # break
        # print time
    # print time
    # break
    results.append(time)

f = open("A-large.out", 'w')
for i, r in enumerate(results):
    f.write("Case #%d: %d\n" % (i+1, r))
f.close()