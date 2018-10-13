import sys
import math

def solve(line):
    # Form sequence and bot order.
    tokens = line.split(' ')
    buttons = int(tokens[0])
    
    sequence = []
    total_time = 0
    for i in range(1, len(tokens), 2):
        sequence.append((tokens[i], int(tokens[i + 1])))

    o_banked = 0
    b_banked = 0

    o = 1
    b = 1
        
    for t in range(len(sequence)):
        robot = sequence[t][0]
        button = sequence[t][1]
            
        if robot == "O":
            move_time = int(math.fabs(button - o))
            move_time -= o_banked
            if move_time < 0:
                move_time = 0
            b_banked += move_time + 1
            total_time += move_time + 1
            o = button
            o_banked = 0
        else:
            move_time = int(math.fabs(button - b))
            move_time -= b_banked
            if move_time < 0:
                move_time = 0
            o_banked += move_time + 1
            total_time += move_time + 1
            b = button
            b_banked = 0
            
        print "%s %s%s %s %s %s %s %s" % (t, robot, button, o, o_banked, b, b_banked, total_time)
                            
    return int(total_time)

if __name__ == '__main__':
    input = sys.argv[1]
    output = "output.txt"
    infile = open(input, "r")
    outfile = open(output, "w")

    cases = int(infile.readline())
    for case in range(cases):
        line = infile.readline()
        answer = solve(line)
        answer = "Case #%s: %s\n" % (case + 1, answer)
        outfile.write(answer)
        print answer

    outfile.close()
