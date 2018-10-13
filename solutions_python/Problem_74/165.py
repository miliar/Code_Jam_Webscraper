"""
Jonathan Simowitz

Google Code Jam 2011
Problem A. Bot Trust
"""

import os

"""
Return the position this robot needs to
travel to.
"""
def findGoal(robot, data):
    for i in range(0, len(data), 2):
        if (data[i] == robot):
            return int(data[i+1])
    #no goals left for that robot
    return -1

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data):
    time = 0

    data = data.split(" ")
    num_switches = int(data.pop(0))
    blue_pos = 1
    orange_pos = 1
    blue_goal = -1
    orange_goal = -1
    orange_skip = False
    blue_skip = False
    
    while (num_switches > 0):
        throw_switch = False
        #determine what orange does
        if (not orange_skip):
            orange_goal = findGoal('O', data)
            orange_skip = True

        #determine what blue does
        if (not blue_skip):
            blue_goal = findGoal('B', data)
            blue_skip = True

        #Orange action
        if (orange_pos < orange_goal):
            orange_pos += 1
        elif (orange_pos > orange_goal):
            orange_pos -= 1
        elif (data[0] == 'O'):
                #orange throws its switch
                throw_switch = True
                orange_skip = False

        #Blue action
        if (blue_pos < blue_goal):
            blue_pos += 1
        elif (blue_pos > blue_goal):
            blue_pos -= 1
        elif (data[0] == 'B'):
                #blue throws its switch
                throw_switch = True
                blue_skip = False

        if (throw_switch):
            num_switches -= 1
            data.pop(0)
            data.pop(0)
                
        time += 1    
    
    return str(time)

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "A-large.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    Heading = True
    test_num = 1

    #Iterate through the input file
    while True:
        #read input one line at a time
        line = rf.readline()
        line = line.strip()

        if not line:
            #end of file

            #close input file
            rf.close()
            #close output file
            wf.close()
            break
        else:            
            #process the line
            if Heading:
                Heading = False
                NUM_TEST_CASES = int(line)
            else:
                wf.write("Case #" + str(test_num) +": " + process(line) + "\n")
                test_num += 1
            
main()
