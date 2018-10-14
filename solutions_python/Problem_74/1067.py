f = open('A-large.in', 'r')
out = open('q1.out', 'w')
num_cases = int (f.readline())

for i in range(num_cases):
    instructions = f.readline().strip("\n").split(' ')
    num_buttons = int(instructions.pop(0))
    sequence = []
    for j in range(0, num_buttons):
        sequence.append((instructions.pop(0), int(instructions.pop(0))))
    
    time = 0
    done = False
    
    o_pos = 1
    b_pos = 1
    
    while not done:
        o_next_step = None
        b_next_step = None
        for step in sequence:
            if step[0] == 'O' and not o_next_step:
                o_next_step = step
            if step[0] == 'B' and not b_next_step:
                b_next_step = step
            if b_next_step and o_next_step:
                break
        
        if sequence[0][0] == 'O' and o_pos == sequence[0][1]:
            sequence.pop(0)
        elif sequence[0][0] == 'B' and b_pos == sequence[0][1]:
            sequence.pop(0)
        
        if o_next_step:
            if o_pos < o_next_step[1]:
                o_pos = o_pos + 1  
            elif o_pos > o_next_step[1]:
                o_pos = o_pos - 1      
        
        if b_next_step:
            if b_pos < b_next_step[1]:
                b_pos = b_pos + 1
            elif b_pos > b_next_step[1]:
                b_pos = b_pos - 1
            
        time = time + 1
            
        if len(sequence) == 0:
            done = True
            
    
    out.write("Case #%d: %d\n" % (i+1, time))