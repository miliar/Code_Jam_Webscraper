'''
Created on 13 sep 2009

@author: magnus
'''
import sys

class Solver(object):
    
    def __init__(self, test):
        xm, ym, zm = 0,0,0
        xvm, yvm, zvm = 0,0,0
        for fly in test:
            (x, y, z, xv, yv, zv) = fly
            xm = xm + x
            ym = ym + y
            zm = zm + z
            xvm = xvm + xv 
            yvm = yvm + yv
            zvm = zvm + zv
        self.xm = float(xm) / len(test)
        self.ym = float(ym) / len(test)
        self.zm = float(zm) / len(test)
        self.xvm = float(xvm) / len(test)
        self.yvm = float(yvm) / len(test)
        self.zvm = float(zvm) / len(test)
        
        #print self.xm, self.ym, self.zm, self.xvm, self.yvm, self.zvm
        #print "-----------"
        
    def get_solution(self):
        try:
            t = -(self.xm*self.xvm + self.ym*self.yvm + self.zm*self.zvm) / (self.xvm*self.xvm + self.yvm*self.yvm + self.zvm*self.zvm)
        except:
            t = 0.0000000000001
        if t < 0:
            t = 0.0000000000001
        return ((self.xm + self.xvm*t)**2 + (self.ym + self.yvm*t)**2 + (self.zm + self.zvm*t)**2)**.5, t 
    
def get_tests():
    tests=[]
    input_file = open(sys.argv[1])
    test_numbers = int(input_file.readline().strip())
    for test_number in range(test_numbers):
        test = []
        fly_number = int(input_file.readline().strip())
        for index in range(fly_number):
            line = input_file.readline().strip()
            fly = [int(value) for value in line.split()]
            test.append(fly)
        tests.append(test)
    return tests
            
if __name__ == '__main__':
    tests = get_tests()
    index = 1
    for test in tests:
        solver = Solver(test)
        d, t = solver.get_solution()
        print "Case #" + str(index)+ ": " + str(d) + " " + str(t)
        index = index + 1
