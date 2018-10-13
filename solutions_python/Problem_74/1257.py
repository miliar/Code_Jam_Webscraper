import sys
import os

debug = False

preffix = 'A-large'
f = open('%s.in' % preffix)
o = open('%s.out' % preffix, 'w')

file_lines = [x.strip('\n\t') for x in f.readlines()]
# print file_lines

# The total of test cases is always at the first line.
test_cases = int(file_lines.pop(0))

def next_robots_move(actual_command, full_sequence):
    sliced_sequence = full_sequence[actual_command:]
    first = sliced_sequence[0]
    second = None
    for item in sliced_sequence:
        if item[0] != first[0]:
            second = item
            break
    return first, second

for test_case_number in range(test_cases):
    positions = {'O': 1, 'B': 1}
    time = 1
    
    commands = file_lines[test_case_number]
    commands = commands.split()
    buttons_number = int(commands.pop(0))
    # print buttons_number
    # print commands
    
    commands = zip(commands[::2], [int(x) for x in commands[1::2]])
    if debug:
        print commands
    
    actual_command = 0
    
    next_move, next_next_move = next_robots_move(actual_command, commands)
    # print next_move, next_next_move
    while True:
        if debug:
            print time
        
        if positions.get(next_move[0]) == next_move[1]:
            if debug:
                print 'Robot %s push the button %s' % (next_move[0], next_move[1])
            actual_command += 1
            if actual_command == len(commands):
                break
        
        if next_move[1] > positions.get(next_move[0]):
            positions[next_move[0]] += 1
            if debug:
                print 'Robot %s move to the button %s' % (next_move[0], positions[next_move[0]])
        if next_move[1] < positions.get(next_move[0]):
            positions[next_move[0]] -= 1
            if debug:
                print 'Robot %s move to the button %s' % (next_move[0], positions[next_move[0]])
        
        if next_next_move:
            if positions.get(next_next_move[0]) == next_next_move[1]:
                if debug:
                    print 'Robot %s stay at button %s' % (next_next_move[0], next_next_move[1])
            if next_next_move[1] > positions.get(next_next_move[0]):
                positions[next_next_move[0]] += 1
                if debug:
                    print 'Robot %s move to the button %s' % (next_next_move[0], positions[next_next_move[0]])
            if next_next_move[1] < positions.get(next_next_move[0]):
                positions[next_next_move[0]] -= 1
                if debug:
                    print 'Robot %s move to the button %s' % (next_next_move[0], positions[next_next_move[0]])
        
        next_move, next_next_move = next_robots_move(actual_command, commands)
        time += 1
    
    o.write('Case #%s: %s\n' % (test_case_number+1, time))
    # b_command = next_robot_move(actual_command, commands, 'B')
    # o_command = next_robot_move(actual_command, commands, 'O')
    # 
    # print b_command, o_command
    

    # commands[actual_command]
    # 
    # for command in commands:
    #     robot = command[0]
    #     button_position = command[1]
    #     while True:
    #         print time
    #         if positions[robot] == button_position:
    #             print 'Robot %s pushed the button %s' % (robot, button_position)
    #             time += 1
    #             break
    #         elif positions[robot] > button_position:
    #             positions[robot] -= 1
    #             print 'Robot %s moved to button %s' % (robot, positions[robot])
    #         elif positions[robot] < button_position:
    #             positions[robot] += 1
    #             print 'Robot %s moved to button %s' % (robot, positions[robot])
    #         time += 1
    # 
    # print time
    # print positions
    
    
    # # print i+1
    # comandos = linhas[i+1]
    # 
    # quantidade_comandos = comandos[0]
    # comandos = comandos[1:].split()
    # 
    # tempo = 0
    # 
    # for j in range(int(quantidade_comandos)):
    #     robo = comandos[j]
    #     botao = comandos[j+1]
    #     print robo, botao
    # 
    # # o.write('Case #%d: %s\n' % (i+1, frase))