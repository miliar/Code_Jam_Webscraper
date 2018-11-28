from __future__ import division
from fractions import gcd

def rins():
    return raw_input().strip()

class Walkway(object):
    def __init__(self, beginning, end, speed):
        self.beginning = beginning
        self.end = end
        self.speed = speed
        self.length = end - beginning
    def time_given_base_speed(self, base_speed):
        speed = self.speed + base_speed
        return self.length / speed

def solve_next():
    x, s, r, t, n = [int(ch) for ch in rins().split()]
    walkways=[]
    for i in xrange(n):
        b, e, w = [int(ch) for ch in rins().split()]
        walkways.append(Walkway(b,e,w))
    
    boring_length = x - sum(ww.length for ww in walkways)
    boring_walkway = Walkway(0,boring_length,0)
    walkways.append(boring_walkway)
    walkways.sort(key=lambda ww:-ww.speed)
    time = 0
    running_time = t
    while running_time > 0:
        if not walkways:
            return time
        ww = walkways.pop()
        rt = ww.time_given_base_speed(r)
        if rt > running_time:
            walkways.append(Walkway(0,ww.length - running_time * (ww.speed + r), ww.speed))
            rt = running_time
        time += rt
        running_time -= rt
    while walkways:
        ww = walkways.pop()
        time += ww.time_given_base_speed(s)
    return time

    

def run():
    t = int(rins())
    for i in xrange(t):
        print "Case #{0}: {1}".format(i+1, solve_next())

run()
