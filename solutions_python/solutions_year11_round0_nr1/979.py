#!/usr/bin/python
'''
Created on 2011 5 7

@author: cihancimen
'''

from math import fabs
def testcase(k):
    line = raw_input().split(" ")
    num = int(line[0])
    steps = []
    for i in range(0,num* 2, 2):
        steps.append((line[i+1], int(line[i+2])))
#    print num, steps
    d = {'O':0, 'B':0}
    time = 0
    o_last = 1
    b_last = 1
    for robot, button in steps:
#        print robot," ", button, " | " ,o_last, " " , d['O'], " | " , b_last, " " , d['B'], " | ", time    
        if(robot == 'O'):
            diff = fabs(o_last - button) - d['B']
            if(diff < 0):
                diff = 0
            o_last = button
            d['B'] = 0
        else:
            diff = fabs(b_last - button) - d['O']
            if(diff < 0):
                diff = 0
            b_last = button
            d['O'] = 0
        diff +=1
        d[robot] +=diff
        time += diff
    print 'Case #%d: %d' % (k, time)
        
        
    
        

if __name__ == '__main__':
    num_test= int(raw_input())
    for i in range(num_test):
        testcase(i+1)
        