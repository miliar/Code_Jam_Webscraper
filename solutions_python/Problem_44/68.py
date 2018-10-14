#!/usr/bin/env python

import sys
import math

def main():
    f = open(sys.argv[1])
    lines = f.readlines()
    f.close()
    
    T = int(lines[0])
    
    base = 1
    for t in range(T):
        N = int(lines[base])
        base += 1
        flies = []
        for n in range(N):
            flies.append(map(int, lines[base].split()))
            base += 1
        solution = solve(flies)
        print "Case #%d: %f %f" % (t+1, solution[0], solution[1])

def solve(flies):
    total = []
    
    for i in range(6):
        total.append(sum([fly[i] for fly in flies]))
    
    t = -dot(total[:3], total[3:])
    div = dot(total[3:], total[3:])
    if div != 0.0:
        t /= div
    else:
        t = 0.0
    if t < 0.0:
        t = 0.0
    t = abs(t)
    
    pos = fly_at(total, t)
    for i in range(3):
        pos[i] /= float(len(flies))
    d = distance(pos)
    
    return (d,t)

def dot(p1, p2):
    return float(p1[0]*p2[0] + p1[1]*p2[1] + p1[2]*p2[2])

def fly_at(fly, t):
    result = fly[:3]
    for i in range(3):
        result[i] += t * fly[i+3]
    return result

def distance(fly):
    return math.sqrt(fly[0]**2 + fly[1]**2 + fly[2]**2)

if __name__ == '__main__':
    main()