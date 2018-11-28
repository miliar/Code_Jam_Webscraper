import math
import os

INPUT_DEFINITION = """
T
:cases T
N P
Gs
"""


def serialize_solution(sol):
    # if type(sol) == float:
    #     return '%.9f' % sol
    return str(int(sol))


from collections import Counter as d
import math

def solve_case(case):
    N = case['N']
    P = case['P']
    Gs = case['Gs']
    if type(Gs) == int:
        Gs = [Gs]
    Ms = d([g % P for g in Gs])
    if P == 2:
        return Ms[0] + math.ceil((Ms[1] / 2.0))
    if P == 3:
        return Ms[0] + min(Ms[1], Ms[2]) + math.ceil(abs(Ms[1] - Ms[2]) / 3.0)


def _solve(P, Ms):
    if P == 2:
        if Ms[0] != 0:
            a = Ms.copy()
            a[0] -= 1
            return 1 + _solve(P, a)
        if Ms[1] == 1:
            return 1
        if Ms[1] == 0:
            return 0
        a = Ms.copy()
        a[1] -= 2
        return 1 + _solve(P, a)
    if P == 3:
        if Ms[0] != 0:
            a = Ms.copy()
            a[0] -= 1
            return 1 + _solve(P, a)
        if Ms[1] > 0 and Ms[2] > 0:
            a1 = Ms.copy()
            a1
            r1 = _solve(P, )


def read_arg_smart(arg):
    funcs = (int, float, str)
    for func in funcs:
        try:
            return func(arg)
        except ValueError:
            continue


def read_smart(line):
    args = line.strip().split()
    res = []
    for arg in args:
        res.append(read_arg_smart(arg))
    if len(res) == 1:
        return res[0]
    return res


from collections import namedtuple

StepDefinition = namedtuple('StepDefinition', [
    'labels', 'substeps', 'num_times_func'
])

import re

expr_re = re.compile('([^\+\-\*\/\^\s\d]+)')


def get_num_times_func(s):
    expr = expr_re.sub(r"context['\1']", s)
    def f(context):
        return eval(expr)
    return f


def load_steps(definition):
    return _load_steps(iter(definition.split('\n')))


def _load_steps(lines):
    steps = []
    while True:
        try:
            line = lines.next()
            if line.strip() == '':
                continue
        except StopIteration:
            break
        if not line.startswith(':'):
            args = read_smart(line)
            step = StepDefinition(labels=args, substeps=None, num_times_func=None)
            steps.append(step)
            continue
        sub_label, expr = line.split(' ', 1)
        sub_label = sub_label[1:]
        expr_func = get_num_times_func(expr.strip())
        substeps = _load_steps(lines)
        step = StepDefinition(labels=[sub_label], substeps=substeps, num_times_func=expr_func)
        steps.append(step)
    return steps


def execute_step(step, stream, context):
    if step.substeps is None:
        try:
            line = stream.next()
        except StopIteration:
            return None
        args = read_smart(line)
        if not isinstance(args, list):
            args = [args]
        if type(step.labels) == list:
            result = dict(zip(step.labels, args))
        else:
            result = {step.labels: args if len(args) > 1 else args[0]}
        return result
    num_times = step.num_times_func(context)
    result = {step.labels[0]: []}
    for i in xrange(num_times):
        subresult = {}
        for substep in step.substeps:
            subresult.update(execute_step(substep, stream, subresult) or {})
        result[step.labels[0]].append(subresult)
    return result


def execute_steps(steps, stream):
    result = {}
    for step in steps:
        result.update(execute_step(step, stream, result))
    return result


def get_download_dir():
    return os.path.expanduser('~/Downloads')





def load_problem(input_definition, file_obj):
    file_obj.seek(0)
    steps = load_steps(input_definition)
    problem = execute_steps(steps, file_obj)
    return problem


def yield_prob(input_definition, file_obj):
    problem = load_problem(input_definition, file_obj)
    for i, case in enumerate(problem['cases']):
        answer = solve_case(case)
        answer_s = serialize_solution(answer)
        yield ('Case #%d: ' % (i + 1)) + answer_s


def choose_input_file():
    downloads = get_download_dir()
    choices = []
    for fname in os.listdir(downloads):
        name, ext = os.path.splitext(fname)
        if ext != '.in':
            continue
        choices.append(fname)
    if len(choices) != 1:
        for i in xrange(len(choices)):
            print '%d: %s' % ((i + 1), choices[i])
        inp = int(raw_input('Choose: '))
        choice = choices[inp - 1]
    else:
        choice = choices[0]
    return os.path.join(downloads, choice)


def auto_load_problem():
    inp_file_path = choose_input_file()
    inp_file_obj = open(inp_file_path)
    problem = load_problem(INPUT_DEFINITION, inp_file_obj)
    return problem


def run_problem():
    inp_file_path = choose_input_file()
    inp_file_name, _ = os.path.splitext(os.path.split(inp_file_path)[1])
    out_file_path = inp_file_name + '.out'
    inp_file_obj = open(inp_file_path)
    out_file_obj = open(out_file_path, 'w')
    problem = load_problem(INPUT_DEFINITION, inp_file_obj)
    for i, case in enumerate(problem['cases']):
        answer = solve_case(case)
        answer_s = serialize_solution(answer)
        out_s = 'Case #%d: %s\n' % ((i + 1), answer_s)
        print out_s.strip()
        out_file_obj.write(out_s)
    out_file_obj.close()


if __name__ == '__main__':
    run_problem()
