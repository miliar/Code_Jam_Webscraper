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
            pancakes, K = tuple([x for x in _file.readline().split(" ")])
            arguments.append((_case + 1, (pancakes, int(K))))

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

IMPOSSIBLE="IMPOSSIBLE"

def solve(pancakes, K):
    result = 0
    N = len(pancakes)
    ps = list(pancakes)
    for i in range(N):
        if ps[i] == "-":
            if i + K > N:
                return IMPOSSIBLE
            result += 1
            for j in range(i, i + K):
                ps[j] = "-" if ps[j] == "+" else "+"
    return result

run()
#run(Pool(4))
