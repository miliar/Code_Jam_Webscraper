from sys import argv, exit

def try_int(s):
    try:
        return int(s)
    except:
        return s

def parse_input(content=None, dynamic=False, smart=True):
    if content is None:
        file_name = argv[1]
        lines = open(file_name).read().split('\n')[0:-1]
    else:
        lines = content.split('\n')
    
    nb_inputs = int(lines[0])
    lines = lines[1:]
    
    # Number of lines per case
    if not dynamic:
        p = len(lines) / nb_inputs
        assert  p * nb_inputs == len(lines)
    
    line_nb = 0
    
    for i in range(nb_inputs):
        if dynamic:
            line = map(try_int, lines[line_nb].split(' '))
            p = int(line[0])
            if len(line) > 1:
                p += 1
            else:
                # I do not take a line that contain only the number of lines
                line_nb += 1
        case_lines = lines[line_nb:line_nb+p]
        if smart:
            smart_func = lambda x: x if len(x) != 1 else x[0]
        else:
            smart_func = lambda x: x
        case = [smart_func(map(try_int, line.split(' '))) for line in case_lines]
        
        if not dynamic and p == 1:
            case = case[0]
        
        line_nb += p
        yield case

'''

'''

def lookup(ins, r, i):
    if ins[i][0] == r:
        return ins[i][1]
    elif i+1 < len(ins):
        return lookup(ins, r, i+1)

def other(r):
    if r == 'O':
        return 'B'
    elif r == 'B':
        return 'O'


def solve(case):
    case = case[1:]
    ins = []
    for i, c in enumerate(case):
        if i % 2 == 0:
            ins.append((c, case[i+1]))
    
    positions = [1, 1]
    n = 0
    
    def move(ri, goal):
        if positions[ri] > goal:
            positions[ri] -= 1
        elif positions[ri] < goal:
            positions[ri] += 1
    
    for i, (r, k) in enumerate(ins):
        ri = 'OB'.index(r)
        other_goal = lookup(ins, other(r), i)
        other_ri = 1 if ri == 0 else 0
        
        while positions[ri] != k:
            if other_goal is not None:
                move(other_ri, other_goal)
            move(ri, k)
            n += 1
        
        if other_goal is not None:
            move(other_ri, other_goal)
        n += 1
            
    return n
                

def test():
    pass

if __name__ == '__main__':
    if len(argv) < 2:
        test()
        exit()

    for i, case in enumerate(parse_input()):
        case_nb = 'Case #%i: ' % (i+1)
        result = solve(case)
        if type(result) is list:
            result = ' '.join(map(str, result))
        else:
            result = str(result)
        print case_nb + result
