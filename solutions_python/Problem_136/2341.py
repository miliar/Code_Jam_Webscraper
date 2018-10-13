import itertools
import math
import operator
import decimal

class CookieClicker:

    def __init__(self):
        self.inputFile = open('input.txt','r')
        self.outputFile = open('output.txt','w')
        numTestCases = int(self.inputFile.readline())
        print 'numTestCases', numTestCases
        for testCase in range(0, numTestCases):
            self.testCase = testCase+1
            print self.testCase
            self.readCase()
            self.solveCases()

    def readCase(self):
        [self.C, self.F, self.X] = [float(x) for x in self.inputFile.readline().split(' ')]
        print 'C=%s, F=%s, X=%s'%(self.C, self.F, self.X)

    def solveCases(self):
        self.rate = 2
        self.cookies = 0
        self.time = 0
        #self.recurse()

        '''
            250 + 83.33 + 50
            2 -> 6 -> 10 -> 14

            500/(2+4*0) + 500/(2+4*1) + 500/(2+4*2) + {500/(2+4*3) + 2000/(2+4*4)}

            500/(2+4*0) + 500/(2+4*1) + 500/(2+4*2) + {2000/(2+4*3)}

            self.C/(2+self.F*i)
        '''

        i = 0
        running = True
        while (running):
            print '-----'

            print 'Iteration: %s'%(i+1)
            print 'Current Rate: %s'%(self.rate)

            buyFarm = False

            potential = (self.X/(self.rate + self.F)) + self.C/self.rate
            current = self.X/self.rate

            if potential < current:
                buyFarm = True

            print 'Buy Farm: %s'%buyFarm

            if buyFarm:
                time = self.C/self.rate
                self.time += time
                self.rate += self.F
            else:
                time = self.X/self.rate
                self.time += time
                running = False

            i += 1

            print 'Time: %s'%time
            print 'Total Time: %s'%self.time
            print 'New Rate: %s'%self.rate

            print '-----'

        self.time = decimal.Decimal(self.time)
        self.time = round(self.time, 7)
        self.answer = self.time

        self.printAnswer()

    def recurse(self):
        pass

    def printAnswer(self):
        outputString = 'Case #%d: %s\n'%(self.testCase,self.answer)
        self.outputFile.write(outputString)
        print outputString

if __name__ == '__main__':
    cookieClicker = CookieClicker()