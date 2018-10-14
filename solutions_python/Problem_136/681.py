#!/usr/bin/python
#! - * - coding: utf-8 - * -

class Bot(object):
    def __init__(self):
        self.C, self.F, self.X = self.get_input()
        self.time = 0.0
        self.rate = 2.0
    def get_input(self):
        return map(lambda x: float(x), raw_input().split())
    def start(self):
        time, rate = 0.0, 2.0
        purchase = self.calculate(rate, self.C) + self.calculate(rate+self.F, self.X)
        npurchase = self.calculate(rate, self.X)
        while purchase < npurchase:
            time += self.calculate(rate, self.C)
            rate = rate + self.F
            purchase = self.calculate(rate, self.C) + self.calculate(rate+self.F, self.X)
            npurchase = self.calculate(rate, self.X)
        time += npurchase 
        return time

    def calculate(self, rate, dst):
        time = dst/rate
        return time
        
if __name__ == "__main__":
    tc = int(raw_input())
    for i in xrange(tc):
        obj = Bot()
        print "Case #%d: %.7f" % (i+1,obj.start())
