def output(f, solution_iter):
    s = list()
    for solution in solution_iter:
        s.append('Case #')
        s.append(str(solution['number']))
        s.append(': ')
        if solution['possible']:
            s.append(str(solution['sean']))
            pass
        else:
            s.append('NO')
            pass
        s.append('\n')
        pass
    f.write(''.join(s))
    pass

def read(f):
    fiter = iter(f)
    cases = int(next(fiter))
    raw_problem_iter = list()
    for x in range(cases):
        numbers = int(next(fiter))
        raw_problem_iter.append({
            'number': x + 1,
            'data': next(fiter).rstrip('\n').split(' '),
        })
        pass
    return iter(raw_problem_iter)

def convert(raw_problem):
    return {
        'number': raw_problem['number'],
        'data': [int(x) for x in raw_problem['data']],
    }

def solution(problem):
    solu = dict()
    solu['number'] = problem['number']
    s = 0
    x = 0
    m = 1000000
    for ele in problem['data']:
        s += ele
        x = x ^ ele
        m = m if m < ele else ele
        pass
    if x:
        solu['possible'] = False
        pass
    else:
        solu['possible'] = True
        solu['sean'] = s - m
        pass
    return solu

def frame(in_file_path, out_file_path):
    solist = list()
    for raw_problem in read(open(in_file_path)):
        p = convert(raw_problem)
        s = solution(p)
        solist.append(s)
        pass
    output(open(out_file_path, 'w'), iter(solist))
    pass
