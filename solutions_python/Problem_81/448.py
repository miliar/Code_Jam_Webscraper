#coding:utf-8

import fileinput
import os
import sys

schedule = dict()
WP = dict(); OWP = dict(); OOWP = dict();

def wp(i):
    if i in WP:
        return WP[i]['wp']
    p = 0.0; w = 0.0
    for j, score in enumerate(schedule[i]):
        if score == '1':
            p = p + 1
            w = w + 1
        elif score == '0':
            p = p + 1
    WP[i] = dict(p=p, w=w, wp=w/p)
    #print 'WP[%d]: %s' % (i, WP[i])
    return WP[i]['wp']
    
def owp(i):
    if i in OWP:
        return OWP[i]
    total = 0.0
    for j, score in enumerate(schedule[i]):
        if score == '1':
            total = total + WP[j]['w'] / (WP[j]['p'] - 1)
        elif score == '0':
            total = total + (WP[j]['w'] - 1) / (WP[j]['p'] - 1)
    OWP[i] = total / WP[i]['p']
    #print 'OWP[%d]: %f' % (i, OWP[i])
    return OWP[i]

def oowp(i):
    if i in OOWP:
        return OOWP[i]
    total = 0.0
    for j, score in enumerate(schedule[i]):
        if score == '1' or score == '0':
            total = total + OWP[j]
    OOWP[i] = total / WP[i]['p']
    #print 'OOWP[%d]: %f' % (i, OOWP[i])
    return OOWP[i]

def process(input, N):
    schedule.clear()
    WP.clear(); OWP.clear(); OOWP.clear();
    RPI = []
    
    for i in range(0,N):
        schedule[i] = input.readline()
        wp(i)
    for i in range(0,N):
        owp(i)
    for i in range(0,N):
        RPI.append(0.25 * WP[i]['wp'] + 0.5 * OWP[i] + 0.25 * oowp(i))
        
    return RPI
    
def solve(input, output):
    for i in range(1,int(input.readline())+1):
        rpi = process(input, int(input.readline()))
        output.write('Case #%d:\n' % i)
        for points in rpi:
            output.write('%.12f\n' % points)
        
if __name__ == '__main__':
    if len(sys.argv) > 1:
        basename, extenstion = os.path.splitext(sys.argv[1])
        solve(open(sys.argv[1]), open('%s.out' % basename, 'w'))
