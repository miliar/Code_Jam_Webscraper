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

def binary(n):
    return map(int, bin(n)[2:])

def bxor(a, b):
    if 1 in (a, b) and 0 in (a, b):
        return 1
    return 0

def resize(a, b):
    if len(a) < len(b):
        a[:0] = [0] * (len(b) - len(a))
    elif len(a) > len(b):
        resize(b, a)

def xor(a, b):
    resize(a, b)
    return [bxor(a[i], b[i]) for i in range(len(a))]

def solve(case):
    case = case[1]
    cs = map(binary, case)
    
    r = []
    for c in cs:
        r = xor(r, c)
    
    if 1 not in r:
        case.sort()
        return sum(case) - case[0]
    return 'NO'

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
