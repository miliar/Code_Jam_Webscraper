#! /usr/bin/env python

if __name__== "__main__":
    testcases = int(input())
    for t in range(testcases):
        line = raw_input()
        line = line.split()
        n_steps = int(line[0])
        line = line[1:]
        orange_pos = 1
        blue_pos = 1
        total_steps = 0
        partial_steps = 0
        
        if line[0] == 'O':
            orange_button = int(line[1])
            current_steps = orange_button - orange_pos + 1
            orange_pos = orange_button
        else:
            blue_button = int(line[1])
            current_steps = blue_button - blue_pos + 1
            blue_pos = blue_button
        last_bot = line[0]
        total_steps += current_steps
        partial_steps = current_steps
        
        for i in range(2, n_steps * 2, 2):
            current_steps = 0
            if line[i] == 'O':
                orange_button = int(line[i+1])
                current_steps = abs(orange_button - orange_pos) + 1
                orange_pos = orange_button
            else:
                blue_button = int(line[i+1])
                current_steps = abs(blue_button - blue_pos) + 1
                blue_pos = blue_button
                
            if line[i] == last_bot:
                partial_steps += current_steps
                total_steps += current_steps
            else:
                last_bot = line[i]
                if current_steps > partial_steps:
                    total_steps = total_steps - partial_steps + current_steps
                    partial_steps = current_steps - partial_steps
                else:
                    total_steps += 1
                    partial_steps = 1
                    
        print "Case #%d: %d" %(t+1, total_steps)

