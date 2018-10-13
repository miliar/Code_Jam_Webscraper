#!/usr/bin/python

import sys

ipt = []
src = []


def read():
    return sys.stdin.readlines()

def test( step_count, casesteps ):
    orange_location = 1
    blue_location = 1
    orange_time = 0
    blue_time = 0
    last_color = ''
    plan_time = 0
    for i in range( step_count ):
        step_color = casesteps[ i*2 + 1 ]
        step_meter = int( casesteps[ i*2 + 2 ] )
        if step_color == 'O':
            plan_time = abs( orange_location - step_meter) + 1 + orange_time
            if last_color == 'B' and plan_time <= blue_time:
                plan_time = blue_time + 1
            orange_time = plan_time
            orange_location = step_meter
            last_color = 'O'
        else:
            plan_time = abs( blue_location - step_meter) + 1 + blue_time
            if last_color == 'O' and plan_time <= orange_time:
                plan_time = orange_time + 1
            blue_time = plan_time
            blue_location = step_meter
            last_color = 'B'
    return str( max( blue_time, orange_time ) )

def runtest():
    for x in range(cases):
        #TODO :implement test code
        inputline = ipt[ x + 1 ][:-1]
        casesteps = inputline.split()
        step_count = int( casesteps[0] )
        ret = test( step_count, casesteps )
        print "Case #" + str(x + 1) + ": " + ret

if __name__ == '__main__':
    ipt = read()
    cases = int( ipt[0] )
    runtest()



