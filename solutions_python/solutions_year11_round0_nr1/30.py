'''
Created on May 6, 2011

@author: mk
'''


def solve(fin, fout):
    cases = int(fin.readline())
    for index in range(cases):
        line = fin.readline().strip().split()
        fout.write(solveCase(index+1, line))

def solveCase(index, line):
    num_buttons = int(line[0])
    buttons = [(line[1 + 2*i], int(line[2 + 2*i]))
                for i in range(num_buttons)]
    count = 0
    location_o, location_b = 1, 1
    while buttons:
        robot_color, button_location = buttons[0]
        if robot_color == 'O':
            elapsed = abs(location_o - button_location) + 1
            count += elapsed
            location_o = button_location
            b_next_buttons = [b[1] for b in buttons if b[0] == 'B']
            if b_next_buttons:
                b_next_button = b_next_buttons[0]
                if abs(location_b - b_next_button) <= elapsed:
                    location_b = b_next_button
                else:
                    if location_b < b_next_button:
                        location_b += elapsed
                    else:
                        location_b -= elapsed
        elif robot_color == 'B':
            elapsed = abs(location_b - button_location) + 1
            count += elapsed
            location_b = button_location
            o_next_buttons = [b[1] for b in buttons if b[0] == 'O']
            if o_next_buttons:
                o_next_button = o_next_buttons[0]
                if abs(location_o - o_next_button) <= elapsed:
                    location_o = o_next_button
                else:
                    if location_o < o_next_button:
                        location_o += elapsed
                    else:
                        location_o -= elapsed
        buttons = buttons[1:]
    
    return "Case #{0}: {1}\n".format(index, count)



if __name__ == '__main__':
    import sys
    solve(sys.stdin, sys.stdout)