#!/usr/bin/env python
import sys
import re

class TestCase:
    n_buttons_pattern = re.compile('^(\\d+)\\s+(.*)$')
    command_pattern = re.compile('^\\s*(O|B)\\s+(\\d+)(.*)$')

    def __init__(self, case_number, input_line):
        match = TestCase.n_buttons_pattern.match(input_line)
        n_buttons = int(match.group(1))
        command_line = match.group(2)
        commands = []
        blue_commands = []
        orange_commands = []
        blue_pos = 1
        orange_pos = 1
        for i in range(n_buttons):
            match = TestCase.command_pattern.match(command_line)
            command = (match.group(1), int(match.group(2)))
            commands.append(command)
            if (command[0] == 'B'):
                blue_commands.append(command) 
            else:
                orange_commands.append(command) 
            command_line = match.group(3)
        seconds = 0
        while (len(blue_commands) > 0) or (len(orange_commands) > 0): # one 'second' loop
            turn_holder = commands[0][0]
            #handle blue
            if (len(blue_commands) > 0):
                if (blue_commands[0][1] == blue_pos):
                    if (turn_holder == blue_commands[0][0]):
                        #push the button
                        commands.remove(blue_commands.pop(0))
                else:
                    if blue_commands[0][1] > blue_pos:
                        blue_pos += 1
                    elif blue_commands[0][1] < blue_pos:
                        blue_pos -= 1

            #handle orange
            if (len(orange_commands) > 0):
                if (orange_commands[0][1] == orange_pos):
                    if (turn_holder == orange_commands[0][0]):
                        #push the button
                        commands.remove(orange_commands.pop(0))
                else:
                    if orange_commands[0][1] > orange_pos:
                        orange_pos += 1
                    elif orange_commands[0][1] < orange_pos:
                        orange_pos -= 1

            seconds += 1

        print('Case #' + str(case_number) + ': ' + str(seconds))

if len(sys.argv) < 2:
    print('Please specify input file')
    exit()

try:
    f = open(sys.argv[1])
except:
    print('Failed to open input file')
    exit()

test_cases = []
n_test_cases = int(f.readline())
for i in range(n_test_cases):
    test_cases.append(TestCase(i+1, f.readline()))

f.close()
