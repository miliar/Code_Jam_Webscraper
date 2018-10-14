#!/usr/bin/env python
import math

from parallels import par

class ProblemB:
    def read(self):
        row = raw_input().split()
        self.N, self.V, self.X = int(row[0]), float(row[1]), float(row[2])
        self.taps = []
        for i in range(self.N):
            self.taps.append(map(float,raw_input().split()))
    def solve(self):
        if False:#self.N==1:
            if self.X==self.taps[0][1]:
                time = self.V/self.taps[0][0]
                return "%.12f" % time
            else:
                return "IMPOSSIBLE"
        elif False:#self.N==2:
            temp1 = self.taps[0][1]
            temp2 = self.taps[1][1]
            sp1 = self.taps[0][0]
            sp2 = self.taps[1][0]
            if temp1==self.X and temp2==self.X:
                time = self.V/(sp1+sp2)
                return "%.12f" % time
            if temp1==self.X:
                time = self.V/sp1
                return "%.12f" % time
            if temp2==self.X:
                time = self.V/sp2
                return "%.12f" % time
            if (temp1-self.X)*(temp2-self.X)>0:
                return "IMPOSSIBLE"
            val1 = abs(temp1-self.X)*sp1
            val2 = abs(temp2-self.X)*sp2
            if val1<val2:
                sp2w = sp1 * abs(temp1-self.X) / abs(temp2-self.X)
                time = self.V / (sp1+sp2w)
                return "%.12f" % time
            else:
                sp1w = sp2 * abs(temp2-self.X) / abs(temp1-self.X)
                time = self.V / (sp2+sp1w)
                return "%.12f" % time
        else:
            smallerVal = 0.0
            smallerSpeed = 0.0
            smallers = []
            biggerVal = 0.0
            biggerSpeed = 0.0
            biggers = []
            equalSpeed = 0.0
            for tap in self.taps:
                if tap[1]<self.X:
                    smallerSpeed += tap[0]
                    smallerVal += abs(tap[1]-self.X)*tap[0]
                    smallers += [tap]
                if tap[1]==self.X:
                    equalSpeed += tap[0]
                if tap[1]>self.X:
                    biggerSpeed += tap[0]
                    biggerVal += abs(tap[1]-self.X)*tap[0]
                    biggers += [tap]
            speed = 0.0
            speed += equalSpeed
            if smallerVal>biggerVal:
                smallers = sorted(smallers,key=lambda x: -x[1])
                smallerSpeedE = 0.0
                smallerValE = 0.0
                for tap in smallers:
                    curVal = abs(tap[1]-self.X)*tap[0]
                    if smallerValE+curVal<=biggerVal:
                        smallerValE += curVal
                        smallerSpeedE += tap[0]
                    elif smallerValE<biggerVal:
                        missVal = biggerVal-smallerValE
                        smallerValE += missVal
                        smallerSpeedE += tap[0]*(missVal/curVal)
                speed += biggerSpeed
                speed += smallerSpeedE
            else:
                biggers = sorted(biggers,key=lambda x: x[1])
                biggerSpeedE = 0.0
                biggerValE = 0.0
                for tap in biggers:
                    curVal = abs(tap[1]-self.X)*tap[0]
                    if biggerValE+curVal<=smallerVal:
                        biggerValE += curVal
                        biggerSpeedE += tap[0]
                    elif biggerValE<biggerVal:
                        missVal = smallerVal-biggerValE
                        biggerValE += missVal
                        biggerSpeedE += tap[0]*(missVal/curVal)
                speed += smallerSpeed
                speed += biggerSpeedE

            if speed == 0.0:
                return "IMPOSSIBLE"
            else:
                return "%.12f" % (self.V/speed)


if __name__ == '__main__':
    par.seq(ProblemB)