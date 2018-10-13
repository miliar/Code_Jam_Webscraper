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
            N, P = tuple([int(x) for x in _file.readline().split(" ")])
            groups = tuple([int(x) for x in _file.readline().split(" ")])
            arguments.append((_case + 1, (N, P, groups)))

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

def by_remainder(P, groups):
    res = [0] * P
    for g in groups:
        for r in range(P):
            if g % P == r:
                res[r] += 1
    return tuple(res)

def fresh(group_count, group_size):
    res = group_count // group_size
    if group_count % group_size != 0:
        res += 1
    return res

def solve2(groups):
    n0, n1 = by_remainder(2, groups)
    return n0 + fresh(n1, 2)

def solve3(groups):
    n0, n1, n2 = by_remainder(3, groups)
    return n0 + min(n1, n2) + fresh(max(n1, n2) - min(n1, n2), 3)

def solve4(groups):
    n0, n1, n2, n3 = by_remainder(4, groups)
    res = n0 + min(n1, n3) + n2 // 2
    R13 = max(n1, n3) - min(n1, n3)
    R2 = n2 % 2
    if R13 >= 2 and R2 == 1:
        res += 1
        R13 -= 2
        R2 -= 1
    F = fresh(R13, 4)
    if F == 0 and R2 == 1:
        res += 1
    else:
        res += F
    return res

def solve(N, P, groups):
    if P == 2:
        return solve2(groups)
    if P == 3:
        return solve3(groups)
    if P == 4:
        return solve4(groups)

run()
#run(Pool(4))

print(solve4([1, 1, 2]), 1)
print(solve4([1, 2]), 1)
print(solve4([1, 3, 1, 2]), 2)
print(solve4([1, 3, 1, 1, 2]), 2)
print(solve4([1, 3, 1, 1, 2, 1]), 3)
print(solve4([0, 1, 3, 1, 1, 2, 1]), 4)
print(solve4([0, 1, 3, 1, 2]), 3)
print(solve4([0, 2]), 2)
print(solve4([0, 2, 2]), 2)
print(solve4([0, 2, 3]), 2)
print(fresh(0, 4), 0)
