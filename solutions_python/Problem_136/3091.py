import math
import sys

def readline():
    return sys.stdin.readline().strip()

def readint():
    return map(int, readline().split(" "))

def readfloat():
    return map(float, readline().split(" "))

cases = readint()[0]

class Simulator:
    def __init__(self, c, f, x):
        self.farm_cost = c
        self.farm_rate = f
        self.target = x

    def simulate(self, n):
        t = 0.0
        cookies = 0
        cps = 2.0
        farms_bought = 0
        while cookies < self.target:
            # print "%f %f %f" % (cookies, t, cps)
            # print self.target
            time_to_buy_farm = (self.farm_cost - cookies)/cps
            time_to_target = (self.target - cookies)/cps
            
            if time_to_buy_farm < time_to_target and farms_bought < n:
                cookies = 0
                t += time_to_buy_farm
                cps += f
                farms_bought += 1
            else:
                t += time_to_target
                cookies += time_to_target * cps
        return t

def c_t(x,n,c,f):
    r = 0.0
    for i in range(0, n):
        r += c/(2+f*i)
    r += x/(2+f*n)
    return r

def c_n(x,c,f):
    r = (f*x-f*c-2*c)/(f*c)
    r = math.ceil(r)
    r = int(r)
    if r < 0:
        r = 0
    return r

for case in range(cases):
    c, f, x = readfloat()
    
    n = c_n(x,c,f)
    t = c_t(x,n,c,f)

    # simulator = Simulator(c,f,x)
    # s = []
    # for i in range(1, 1000):
    #     s.append(simulator.simulate(i))
    # t = min(s)

    print "Case #%d: %f" % (case + 1, t)
