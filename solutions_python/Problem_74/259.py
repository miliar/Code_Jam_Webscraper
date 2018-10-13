#!/usr/bin/env python

import sys

def read_line():
    return sys.stdin.readline().rstrip( '\n' )

def read_integer():
    return int( read_line() )

def read_integers():
    return [ int( x ) for x in read_line().split() ]

def read_strings():
    return read_line().split()

def input_string_stack():
    data = []
    for line in sys.stdin.readlines():
        data.extend( line.split() )
    data.reverse()
    return data

def input_integer_stack():
    return [ int( x ) for x in read_string_stack() ]


robot_indices = { 'B' : 0, 'O' : 1 }
T = read_integer()
for t in range( T ):
    buttons = read_strings()
    button_total = int( buttons.pop( 0 ) )
    robot_buttons = [ [], [] ]
    button_index = 0
    while buttons:
        robot_index = robot_indices[ buttons.pop( 0 ) ]
        button = int( buttons.pop( 0 ) )
        robot_buttons[ robot_index ].append( ( button_index, button ) )
        button_index += 1
    steps = 0
    button_index = 0
    robot_positions = [ 1, 1 ]
    #print robot_buttons
    while button_index < button_total:
        #print
        #print 'Button index\t', button_index
        #print 'Positions\t', robot_positions
        pressed = False
        for robot_index in [ 0, 1 ]:
            if robot_buttons[ robot_index ]:
                target_index, target_button = robot_buttons[ robot_index ][ 0 ]
                #print '\t', target_index, target_button
                if robot_positions[ robot_index ] < target_button:
                    robot_positions[ robot_index ] += 1
                elif robot_positions[ robot_index ] > target_button:
                    robot_positions[ robot_index ] -= 1
                elif button_index == target_index:
                    #print '*'
                    robot_buttons[ robot_index ].pop( 0 )
                    pressed = True
        if pressed:
            button_index += 1
        steps += 1
    print 'Case #%i: %i' % ( t + 1, steps )