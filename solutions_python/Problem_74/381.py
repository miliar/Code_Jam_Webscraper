'''
Created on 7-may-2011

@author: Joachim Van Herwegen
'''

def parse_line(line):
    parts = line.split()[1:]
    output = []
    for i in xrange(0,len(parts),2):
        output.append((parts[i],int(parts[i+1])))
    return output

def get_next_pos(input, robots):
    output = dict([(x, None) for x in robots])
    i = 0
    while robots and i < len(input):
        robot = input[i][0]
        if robot in robots and not output[robot]:
            output[robot] = input[i][1]
        i += 1
    return output

def other_robot(robot):
    return 'B' if robot == 'O' else 'O'      

def calc_result(input):
    steps = 0
    pos = {'B':1, 'O':1}
    next_pos = get_next_pos(input, ['O', 'B'])
    while input:
        steps += 1
        next_robot = input[0][0]
        if pos[next_robot] == next_pos[next_robot]:
            del input[0]
            next_pos.update(get_next_pos(input,[next_robot]))
        elif pos[next_robot] < next_pos[next_robot]:
            pos[next_robot] += 1
        else:
            pos[next_robot] -= 1
            
        other = other_robot(next_robot)
        if next_pos[other]:
            if pos[other] < next_pos[other]:
                pos[other] += 1
            elif pos[other] > next_pos[other]:
                pos[other] -= 1
    return steps


def main():
    file = open("bot_trust_large.txt", 'rU')
    file.readline()
    results = []
    for line in file:
        input = parse_line(line)
        results.append(calc_result(input))
    file.close()
    
    output = open("output_bot_trust_large.txt", 'w')
    for i, result in enumerate(results):
        output.write("Case #%d: %d" % (i+1, result))
        if i < len(results)-1:
            output.write("\n")
    output.close()

if __name__ == '__main__':
    main()