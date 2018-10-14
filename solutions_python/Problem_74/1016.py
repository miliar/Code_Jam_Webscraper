def getNextCommand(commands, bot, from_idx):
    if from_idx >= len(commands):
        return None
    for idx, command in enumerate(commands[from_idx:]):
        current_b, _ = command
        if current_b == bot:
            return idx + from_idx
    return None

def calculateTime(commands):
    bot_o_pos = 1
    bot_b_pos = 1
    
    time = 0
    
    current_bot_o_command_idx = getNextCommand(commands, "O", 0)
    current_bot_b_command_idx = getNextCommand(commands, "B", 0)
    
    bot_o_done = False
    bot_b_done = False
    
    if current_bot_o_command_idx == None:
        bot_o_done = True
        active_bot = "B"
    if current_bot_b_command_idx == None:
        bot_b_done = True
        active_bot = "O"
    
    if current_bot_o_command_idx != None and current_bot_b_command_idx != None:
        if current_bot_o_command_idx < current_bot_b_command_idx:
            active_bot = "O"
        else:
            active_bot = "B"
    
    if bot_o_done and bot_b_done:
        return 0
    
    while True:
        time += 1
        if current_bot_o_command_idx != None:
            _, current_bot_o_goal = commands[current_bot_o_command_idx]
        if current_bot_b_command_idx != None:
            _, current_bot_b_goal = commands[current_bot_b_command_idx]
        
        if active_bot == "O":
            if bot_o_pos == current_bot_o_goal:
                current_bot_o_command_idx = getNextCommand(commands, "O", current_bot_o_command_idx + 1)
                if current_bot_o_command_idx == None:
                    bot_o_done = True
                    if bot_b_done:
                        break
                    else:
                        active_bot = "B"
                else:
                    if not current_bot_b_command_idx == None and current_bot_b_command_idx < current_bot_o_command_idx:
                        active_bot = "B"
                    else:
                        active_bot = "O"
            else:
                if bot_o_pos < current_bot_o_goal:
                    bot_o_pos += 1
                else:
                    bot_o_pos -= 1
            if not bot_b_done:
                if bot_b_pos < current_bot_b_goal:
                    bot_b_pos += 1
                elif bot_b_pos > current_bot_b_goal:
                    bot_b_pos -= 1
        else:
            if bot_b_pos == current_bot_b_goal:
                current_bot_b_command_idx = getNextCommand(commands, "B", current_bot_b_command_idx + 1)
                if current_bot_b_command_idx == None:
                    bot_b_done = True
                    if bot_o_done:
                        break
                    else:
                        active_bot = "O"
                else:
                    if not current_bot_o_command_idx == None and current_bot_o_command_idx < current_bot_b_command_idx:
                        active_bot = "O"
                    else:
                        active_bot = "B"
            else:
                if bot_b_pos < current_bot_b_goal:
                    bot_b_pos += 1
                else:
                    bot_b_pos -= 1
            if not bot_o_done:
                if bot_o_pos < current_bot_o_goal:
                    bot_o_pos += 1
                elif bot_o_pos > current_bot_o_goal:
                    bot_o_pos -= 1
    
    return time

for case in xrange(input()):
    input = raw_input().split()
    
    commands = []
    
    num_commands = int(input[0])
    command_inp = input[1:]
    
    for command in range(num_commands):
        commands.append((command_inp[command * 2], int(command_inp[command * 2 + 1])))
    
    res = calculateTime(commands)

    print "Case #%i: %i" % (case+1, res)