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
            N = int(_file.readline())
            arguments.append((_case + 1, (N,)))

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

def step(N):
    digits = list(str(N))
    result = []
    for i in range(len(digits) - 1):
        if digits[i + 1] < digits[i]:
            result.append(digits[i])
            result.extend('0' for d in digits[i+1:])
            return int("".join(result)) - 1
        else:
            result.append(digits[i])
    return N


def solve(N):
    k = N
    while True:
        s = step(k)
        if s == k:
            return s
        k = s

run()
#run(Pool(4))
