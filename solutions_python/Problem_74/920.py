import sys

def dir_from(x, y):
    return cmp(y, x)

def solve(sequence):
    sequence = sequence.split(" ")[1:]
    steps = zip(sequence[::2], sequence[1::2])
    blue_steps = []
    orange_steps = []
    for i, step in enumerate(steps):
        bot, dest = step
        if bot == "B":
            blue_steps.append( (int(dest), i) )
        else:
            orange_steps.append( (int(dest), i) )
    blue_pos = 1
    orange_pos = 1
    blue_i = 0
    orange_i = 0
    total_time = 0
    while blue_i < len(blue_steps) or orange_i < len(orange_steps):
        has_blue = blue_i < len(blue_steps)
        has_orange = orange_i < len(orange_steps)
        
        if has_blue:
            blue_priority = -blue_steps[blue_i][1]
            blue_target = blue_steps[blue_i][0]
            blue_movement = blue_target - blue_pos
            blue_dist = abs(blue_movement)
            if blue_movement < 0:
                blue_dir = -1
            elif blue_movement > 0:
                blue_dir = 1
            else:
                blue_dir = 0
            
        if has_orange:
            orange_priority = -orange_steps[orange_i][1]
            orange_target = orange_steps[orange_i][0]
            orange_movement = orange_target - orange_pos
            orange_dist = abs(orange_movement)
            if orange_movement < 0:
                orange_dir = -1
            elif orange_movement > 0:
                orange_dir = 1
            else:
                orange_dir = 0
        
        if not has_blue:
            orange_move_time = orange_dist
            blue_move_time = orange_move_time + 1
            orange_i += 1
        elif not has_orange:
            blue_move_time = blue_dist
            orange_move_time = blue_move_time + 1
            blue_i += 1
        else:
            if blue_priority < orange_priority:
                orange_i += 1
                orange_move_time = orange_dist
                blue_move_time = orange_move_time + 1
            else:
                blue_move_time = blue_dist
                blue_i += 1
                orange_move_time = blue_move_time + 1
        
        if has_blue:
            blue_pos += blue_dir * min(blue_move_time, blue_dist)
        
        if has_orange:
            orange_pos += orange_dir * min(orange_move_time, orange_dist)
        total_time += max(blue_move_time, orange_move_time)
            
            
    return total_time
        
    return total_time
    
raw_data = "".join(sys.stdin.readlines())
test_cases = raw_data.strip().split("\n")[1:]
for i, test_string in enumerate(test_cases):
    x = solve(test_string)
    print "Case #%i: %s" % (i+1, str(x))