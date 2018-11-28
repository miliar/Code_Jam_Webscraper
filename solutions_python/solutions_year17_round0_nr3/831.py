#!/usr/bin/python

import sys

class Empties(object):
    def __init__(self, n):
        self.empties = {n: 1}
    
    def getMax(self):
        m = 0
        for e, count in self.empties.iteritems():
            assert(count > 0)
            if e>m:
                m = e
        return m

    def getCount(self, n):
        return self.empties[n]

    def decrementBy(self, n, d):
        assert(self.empties[n]>=d)
        self.empties[n] -= d
        if self.empties[n] == 0:
            del(self.empties[n])

    def incrementBy(self, n, i):
        if n in self.empties:
            self.empties[n] += i
        else:
            self.empties[n] = i

def solveBathroom(n, k):
    y = None
    z = None
    empties = Empties(n)
    #print empties.empties
    while k>0:
        m = empties.getMax()
        if m==1:
            z = 0
            y = 0
        else:
            z = m-m/2-1
            y = m/2
        c = empties.getCount(m)
        if k>=c:
            #print "A: %d %d %d: %s" % (k, m, c, str(empties.empties))
            #print "A: %d %d %d" % (k, m, c)
            empties.decrementBy(m, c)
            empties.incrementBy(z, c)
            empties.incrementBy(y, c)
            k -= c
        else:
            #print "B: %d %d %d: %s" % (k, m, c, str(empties.empties))
            empties.decrementBy(m, k)
            empties.incrementBy(z, k)
            empties.incrementBy(y, k)
            k = 0
        #print empties.empties
    return y, z

def main():
    f = open("input.txt")
    numTests = int(f.readline())
    output = ""
    for i in range(numTests):
        [n, k] = f.readline().split(' ')
        n = int(n)
        k = int(k)

        y, z = solveBathroom(n, k)
        output += "Case #%d: %d %d\n" % ((i+1), y, z)

    fout = open("output.txt", "w")
    fout.write(output)

if __name__ == "__main__":
    main()

