import sys
from multiprocessing import Pool

# Add git repository with helpers to path
# The repo is publicly available at git@github.com:marcelka/cocoli.git
sys.path.append("/home/marcelka/projects/cocoli/")

def run(pool=None): # {{{
    inp=sys.argv[1]
    outp="%s.out" % inp.split(".")[0]

    with open(inp, 'r') as _file, open(outp, 'w') as out:
        _cases = int(_file.readline())
        arguments = []
        for _case in range(_cases):
            tpl = tuple([int(x) for x in _file.readline().split(" ")])
            arguments.append((_case + 1, (tpl,)))

        if pool == None:
            results = list(map(solve_wrapper, arguments))
        else:
            results = sorted(
                list(pool.imap_unordered(solve_wrapper, arguments)),
                key=lambda r: r[0])
        assert(len(results) == _cases)
        
        for _case, result in results:
            out.write("Case #%s: %s\n" % (_case, result))

def solve_wrapper(args):
    case_no, _args = args
    print("Solving case #%s" %(case_no))
    return (case_no, solve(*_args))
# }}}

IMPOSSIBLE = "IMPOSSIBLE"

def solve_small(tpl):
    N, R, O, Y, G, B, V = tpl
    ponies = sorted([(R, 'R'), (B, 'B'), (Y, 'Y')])
    a, A = ponies[2]
    b, B = ponies[1]
    c, C = ponies[0]

    x = a - b

    if c < x:
        return IMPOSSIBLE

    c2 = x + (c - x) // 2
    c1 = c - c2

    pool1 = [C] * c1 + [A] * a
    pool2 = [B] * b + [C] * c2
    result = []

    while pool1:
        result.append(pool1.pop())
        if pool2:
            result.append(pool2.pop())
    return ''.join(result)

def solve(tpl):
    return solve_small(tpl)

run()
#run(Pool(4))
