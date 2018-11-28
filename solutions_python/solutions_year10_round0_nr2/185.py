#!/usr/bin/python
import sys
import nzmath.factor.methods as methods

def getT(t):
    dt = map(lambda x: x - min(t), t)
    
    try:
        while 1:
            dt.remove(0)
    except:
        pass

    factors = methods.factor(min(dt))

    T = 1
    for n, m in factors:
        while max(map(lambda x: x%n**m, dt))>0:
            m-=1
        T = T * n**m

    return T
    

def main():
    data = sys.stdin.readlines()
    assert(len(data[1:]) == int(data[0]))
    
    for i, line in enumerate(data[1:]):
        t = map(long, line.split(' '))[1:]
        periodicity = getT(t)
        y = periodicity - t[0]%periodicity
        if y == periodicity:
            y = 0
        
        print "Case #"+str(i+1)+": "+str(y)
             

if __name__ == '__main__':
    main()
