import sys
from multiprocessing import Pool

# Add git repository with helpers to path
# The repo is publicly available at git@github.com:marcelka/cocoli.git
sys.path.append("/home/marcelka/projects/cocoli/")

from memo import memo

def run(pool=None): # {{{
    inp=sys.argv[1]
    outp="%s.out" % inp.split(".")[0]

    with open(inp, 'r') as _file, open(outp, 'w') as out:
        _cases = int(_file.readline())
        arguments = []
        for _case in range(_cases):
            n, k = tuple([int(x) for x in _file.readline().split(" ")])
            arguments.append((_case + 1, (n, k)))

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

@memo
def solve_part(n, k):
    a = (n - 1) // 2
    b = n - 1 - a
    if k == 1:
        return max(a, b), min(a, b)
    ka = (k - 1) // 2
    kb = k - 1 - ka
    result = (10**20, 10**20)
    if ka > 0:
        result = min(result, solve_part(a, ka))
    if kb > 0:
        result = min(result, solve_part(b, kb))
    return result

def solve(n, k):
    return "%s %s" % solve_part(n, k)

run()
#run(Pool(4))

#from random import randint
#
#for i in range(100):
#    n = randint(1, 10**18)
#    k = randint(1, n)
#    print(n, k, solve(n, k))
