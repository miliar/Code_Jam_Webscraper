def check(case):
    if case !=1:
        raw_input()
    maze = []
    for i in range(4):
        maze.append(raw_input())

    hasdot = False
    transport = []
    for line in maze:
        ans, seperate = line_check(line)
        if ans == 'X':
            return 'X won'
        if ans == 'O':
            return 'O won'
        if ans == '.':
            hasdot = True
        transport.append(seperate)

    lines = [[transport[x][i] for x in range(4)] for i in range(4)]
    dia1 = [transport[i][i] for i in range(4)]
    dia2 = [transport[i][3-i] for i in range(4)] 
    lines.append(dia1)
    lines.append(dia2)
    for line in lines:
        ans, seperate = line_check(line)
        if ans == 'X':
            return 'X won'
        if ans == 'O':
            return 'O won'
        if ans == '.':
            hasdot = True
    if hasdot:
        return 'Game has not completed'
    else:
        return 'Draw'
         
def line_check(line):
    count = {}
    seperate = []
    for c in line:
        seperate.append(c)
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    if 'X' in count and (count['X'] == 4 or ('T' in count and count['X'] == 3 and count['T'] == 1)):
        return 'X', seperate
    if 'O' in count and (count['O'] == 4 or ('T' in count and count['O'] == 3 and count['T'] == 1)):
        return 'O', seperate
    if '.' in count:
        return '.', seperate
    return 'F', seperate

if __name__ == '__main__':
    t = int(raw_input())
    for case in range(1, t+1):
        print("Case #{0}: {1}".format(case, check(case)))


