'''
Created on 2011-05-07

@author: Przemyslaw Gorny
'''

import sys

# Read the number of test cases
test_cases = sys.stdin.read().split("\n")
number_of_cases = int(test_cases[0])
for test_case in xrange(1, number_of_cases + 1):
    # read the test case
    case = test_cases[test_case].split(" ")
    
    blue = []
    orange = []
    context = [] 
    
    # number of directives specified in the test case
    directives = int(case[0])
    
    # load the directives
    for directive in xrange(0, directives):
        robot = case[1 + directive*2]
        position = case[2 + directive*2]
        
        if robot == "B":
            blue.append(int(position))
            context.append(robot)
        else:
            orange.append(int(position))
            context.append(robot)
    
          
        
    # initial position = 1, 1 for both   
    position = 0
    moves = 0
    
    # reverse the list to get the stack 
    blue.reverse()
    orange.reverse()
    
          
    blue_robot_position = 1
    desired_blue_position = -1
    orange_robot_position = 1
    desired_orange_position = -1
    while position < len(context):
        # count the new move
        moves += 1
        
        # did they move in this round? if so, they cannot press the button
        blue_moved = False
        orange_moved = False
        
        
        
        # load new position
        if desired_blue_position < 0 and len(blue) > 0:
            desired_blue_position = blue.pop()
            
        if desired_orange_position < 0 and len(orange) > 0:
            desired_orange_position = orange.pop()
                    
        if desired_blue_position > 0: 
            
            if blue_robot_position < desired_blue_position:
                blue_robot_position += 1
                blue_moved = True
            elif blue_robot_position > desired_blue_position:
                blue_robot_position -= 1
                blue_moved = True
            
        if desired_orange_position > 0:
            if orange_robot_position < desired_orange_position :
                orange_robot_position += 1
                orange_moved = True
            elif  orange_robot_position > desired_orange_position :
                orange_robot_position -= 1
                orange_moved = True
        
        # should we press the button?
        if not blue_moved and context[position] == "B" and blue_robot_position == desired_blue_position:     
            # push the blue button
            desired_blue_position = -1
            position += 1
            
        elif not orange_moved and context[position] == "O" and orange_robot_position == desired_orange_position:
            # press the red button
            desired_orange_position = -1
            position += 1
        
    # print the output
    print "Case #" + str(test_case) + ": " + str(moves) 
                                    