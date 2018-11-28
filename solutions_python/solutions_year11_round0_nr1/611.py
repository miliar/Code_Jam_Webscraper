#! /usr/bin/python

import sys, os

f = file(sys.argv[1])
lines = f.readlines()
f.close()

inputData = []
cases = int(lines[0].strip())

pos = 1
for c in range(cases):
    data = lines[pos].strip().split()
    buttons = []
    for j in range(int(data[0])):
        buttons.append([data[1 + j*2], int(data[2 + j*2])])
    inputData.append( buttons )
    pos = pos + 1


def analyse(buttonSequence):
    if buttonSequence[-1][0] == 'B':
        orange_dest = [0] 
        blue_dest = [buttonSequence[-1][1]]
    else:
        orange_dest = [buttonSequence[-1][1]] 
        blue_dest = [0]
    #start at the back
    for robot, button in reversed(buttonSequence[:-1]):
        if robot == 'O':
            orange_dest.insert(0, button)
            blue_dest.insert(0, blue_dest[0])
        else:
            blue_dest.insert(0, button)
            orange_dest.insert(0, orange_dest[0])
    #print(buttonSequence)
    #print(blue_dest)
    #print(orange_dest)
    time = 0
    pos_O = 0
    pos_B = 0
    #print('time,pos_B,pos_O')
    for rb, dest_B, dest_O in zip(buttonSequence, blue_dest, orange_dest):
        #print(time,pos_B,pos_O)
        robot, button = rb
        if robot == 'B':
            dt = abs(pos_B - button) + 1 #+1 for time to press button
            pos_B = button
            if dt < abs(pos_O - dest_O):
                if pos_O > dest_O:
                    pos_O = pos_O - dt
                else:
                    pos_O = pos_O + dt
            else:
                pos_O = dest_O
        else:
            dt = abs(pos_O - button) + 1 #+1 for time to press button
            pos_O = button
            if dt < abs(pos_B - dest_B):
                if pos_B > dest_B:
                    pos_B = pos_B - dt
                else:
                    pos_B = pos_B + dt
            else:
                pos_B = dest_B
        time = time + dt
    return time - 1

output = []
for case,input in enumerate(inputData):
    print('case %i : inputs %s' % (case+1, input))
    res = analyse(input)
    output.append('Case #%i: %i' % (case+1, res))
    print(output[-1])

f = file(sys.argv[1].replace('.in','.out'),'w')
f.write('\n'.join(output))
f.close()
