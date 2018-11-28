
import sys
import collections

import numpy as np

#For debugging.
from IPython.Shell import IPShellEmbed
ipshell = IPShellEmbed()

if len(sys.argv) < 2:
    print('Need an input file!')
    exit()

input_filename = sys.argv[1]
output_filename = input_filename + '.out'

input_file = file(input_filename)
output_file = file(output_filename,'w')

num_cases = int(input_file.readline())



for i in xrange(num_cases):
    #Parse something like this :
    #'4 O 2 B 1 B 2 O 4\n'
    line = input_file.readline().split(' ')
    sequence = collections.deque([((j-1)/2,line[j],int(line[j+1])) for j in xrange(1,len(line),2)])
    orange_sequence = collections.deque(filter(lambda x: x[1] == 'O', sequence))
    blue_sequence = collections.deque(filter(lambda x: x[1] == 'B', sequence))
    
    #Initialize problem.
    orange_pos = 1
    blue_pos = 1
    
    time = 0
    cur_action = sequence.popleft()
    if len(orange_sequence) > 0:
        orange_action = orange_sequence.popleft()
    else:
        orange_action = None
    if len(blue_sequence) > 0:
        blue_action = blue_sequence.popleft()
    else:
        blue_action = None
    while(cur_action != None):
        action_done = False
        #Orange action
        if cur_action[1] == 'O':
            if orange_pos == cur_action[2]:
                #press button.
                action_done = True
            else:
                #move
                orange_pos += np.sign(cur_action[2] - orange_pos)
        elif orange_action != None: 
            if orange_pos == orange_action[2]:
                #wait.
                pass
            else:
                #move in anticipation
                orange_pos += np.sign(orange_action[2] - orange_pos)
    
        #Blue action
        if cur_action[1] == 'B':
            if blue_pos == cur_action[2]:
                #press button
                action_done = True
            else:
                #move
                blue_pos += np.sign(cur_action[2] - blue_pos)
        elif blue_action != None:
            #Can move but not push.
            if blue_pos == blue_action[2]:
                #wait
                pass
            else:
                #move in anticipation
                blue_pos += np.sign(blue_action[2] - blue_pos)
            
        if action_done:
            #if there are actions left.
            if len(sequence) > 0:
                if cur_action [1] == 'O':
                    if len(orange_sequence) > 0:
                        orange_action = orange_sequence.popleft()
                    else:
                        orange_action = None
                else:
                    if len(blue_sequence) > 0:
                        blue_action = blue_sequence.popleft()
                    else:
                        blue_action = None
                cur_action = sequence.popleft()
                
            else:
                #it's over.
                cur_action = None
        
        time +=1
    output_file.write('Case #%i: %i\n'%(i+1,time))
