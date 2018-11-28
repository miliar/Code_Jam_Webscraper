#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      udonko
#
# Created:     13/04/2014
# Copyright:   (c) udonko 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# python3.3.2


class OneTest:
    def __init__(self, c,f,x):
        """
        c is the cost of cookie factory
        f is the addtional number of cookie per sec per factory
        x is target of the number of cockies

        """
        self.initialNumCookiePerSec = 2.0

        self.c = c
        self.f = f
        self.x = x

        self.dic = {}
        self.maxkey = -1

        self.resolve()

    def resolve(self):
        self.result = self.calc()
    def getAnswer(self):
        return self.result

    def calcTimeNFactoryToBuy(self,num_factory, speed):
        if num_factory in self.dic:
            return self.dic[num_factory]
        if self.maxkey != -1:
            time,speed = self.dic[self.maxkey]
        else:
            time = 0


        for i in range(self.maxkey+1, num_factory):
            time += self.c/speed
            speed += self.f
            self.dic[i] = (time, speed)
            self.maxkey = i

        return time, speed

    def calcWithFactory(self,num_factrory,speed, ):
        time, speed =  self.calcTimeNFactoryToBuy(num_factrory, speed)
        return time + self.x / speed

    def calc(self):
        besttime = self.x/self.initialNumCookiePerSec
        lasttime = self.x/self.initialNumCookiePerSec
        num_factory = 0
        while True:
            time = self.calcWithFactory(num_factory, self.initialNumCookiePerSec)
            num_factory += 1
            if time > lasttime:
                break
            lasttime = time
        return lasttime
class Resolve:
    def __init__(self, filename):
        with open(filename, "r") as infile:
            tmp = infile.readline();
            self.t =int(tmp)
            def readStatus():
                tmp = infile.readline();
                c,f,x = list(map(float, tmp.split()))
                return c,f,x
            with open(filename+"out.txt","w") as outfile:
                for i in range(self.t):

                    onetest =  OneTest(*readStatus())
                    tmp = "Case #{0}: {1:.7f}\n".format(i+1 , onetest.getAnswer() )
                    outfile.write(tmp)


def main():
    filename = "B-large.in"
    res = Resolve(filename)

if __name__ == '__main__':
    main()
