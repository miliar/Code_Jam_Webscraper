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

def solve(case):
    C = case[0]
    ts = case[1:C+1]
    D = case[C+1]
    ds = case[C+2:C+2+D]
    es = case[-1]
    try:
        assert len(case) == C + D + 4
    except:
        import ipdb;ipdb.set_trace()
    
    ts_dic = {}
    for t in ts:
        ts_dic[t[:2]] = ts_dic[t[1] + t[0]] = t[2]
    
    ds_dic = {}
    for d in ds:
        if d[0] not in ds_dic:
            ds_dic[d[0]] = set()
        ds_dic[d[0]].add(d[1])
        if d[1] not in ds_dic:
            ds_dic[d[1]] = set()
        ds_dic[d[1]].add(d[0])
    
    r = []
    for e in es:
        r.append(e)
        while len(r) >= 2:
            lasts = ''.join(r[-2:]) 
            if lasts in ts_dic:
                r[-2:] = ts_dic[lasts]
                continue
            
            last = r[-1]
            if last in ds_dic:
                d_set = ds_dic[last]
                if d_set.intersection(r):
                    r = []
            
            break
    
    return '[%s]' % (', '.join(map(str, r)))

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
