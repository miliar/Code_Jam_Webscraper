'''
Created on 06/05/2011

@author: Shimi
'''

import sys

OUTPUT_FILEPATH = 'output_file'
        
def compute_steps(instructions):
    prev_locs = {'B': 1,
                 'O': 1
                 }
    last_streak_steps = {'B': 0,
                            'O': 0
                            }
    
    # just handle the first turn
    last_to_go = instructions[0]
    steps_counter = int(instructions[1]) - 1 + 1 # minus 1 the diff between places, plus 1 for pushing the button
    prev_locs[instructions[0]] = int(instructions[1])
    last_streak_steps[instructions[0]] = int(instructions[1])
    
    for i in range(2, len(instructions) - 1, 2):
        bot = instructions[i]
        new_loc = int(instructions[i + 1])
        steps_needed = abs(new_loc - prev_locs[bot]) + 1 # plus 1 for pushing the button
        # if other bot was last and can move during the other bots actions - does it
        if last_to_go != bot:
            steps_needed -=  last_streak_steps[last_to_go]
            if steps_needed < 1:
                steps_needed = 1
            last_streak_steps[last_to_go] = 0
            last_to_go = bot
            
        prev_locs[bot] = new_loc
        last_streak_steps[bot] += steps_needed
        steps_counter += steps_needed
        
    return steps_counter
        
def main():
    filepath = sys.argv[1]
    input_file = open(filepath, "rb")
    output_file = open(OUTPUT_FILEPATH, "wb")
    lines = input_file.readlines()[1:]
    input_file.close()
    
    for i, line in enumerate(lines):
        tokens = line.split()
        tokens =  tokens[1:]
        output_file.write("Case #%d: " % (i + 1));
        output_file.write('%d' % (compute_steps(tokens)))
        output_file.write('\n')
    
    output_file.close()
    return
        
if __name__ == "__main__":
    main()