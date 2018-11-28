def find_command(commands, color):
    for i in xrange(len(commands)):
        command = commands[i]
        if command == color:
            return int(commands[i+1]), i==0
    return None

def prepare_for_command(command_pos, current_position):
    if command_pos == current_position:
        return True, current_position
    else:
        if command_pos < current_position:
            return False, current_position-1
        else:
            return False, current_position+1

def process(s):
    commands = s.split(' ')[1:]

    o_pos = 1
    b_pos = 1
    
    
    turns = 0
    
    while True:
        next_b_command = find_command(commands, 'B')
        if next_b_command:
            b_command_pos, b_can_execute =  next_b_command
            b_ready, b_pos = prepare_for_command( b_command_pos, b_pos )
        else:
            b_can_execute = False
        
        next_o_command = find_command(commands, 'O')
        if next_o_command:
            o_command_pos, o_can_execute = next_o_command
            o_ready, o_pos = prepare_for_command( o_command_pos, o_pos )
        else:
            o_can_execute = False
        
        if (b_can_execute and b_ready) or (o_can_execute and o_ready):
            commands = commands[2:]
                
        turns += 1
        
        if commands == []:
            break

        
    return turns
    

number_of_cases = int(raw_input())

for case_number in xrange(1, number_of_cases+1):
    s = raw_input()
    result = process(s)
    print "Case #%d: %d" % (case_number, result)
    case_number += 1