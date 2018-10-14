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
            N, C, M = tuple([int(x) for x in _file.readline().split(" ")])
            tickets = []
            for _ in range(M):
                tickets.append((tuple([int(x) for x in _file.readline().split(" ")])))
            arguments.append((_case + 1, (N, C, M, tickets)))

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

from collections import defaultdict

def needed_for(i, k):
    res = k // i
    if k % i != 0:
        res += 1
    return res

def solve(N, C, M, tickets):
    customer_tickets = defaultdict(lambda: 0)
    seat_tickets = defaultdict(lambda: 0)
    for p, b in tickets:
        customer_tickets[b] += 1
        seat_tickets[p] += 1
    rides = max(customer_tickets[i] for i in range(1, C + 1))
    up_to_i = 0
    for i in range(1, N + 1):
        up_to_i += seat_tickets[i]
        rides = max(rides, needed_for(i, up_to_i))
    promotions = 0
    for i in range(1, N + 1):
        promotions += max(0, seat_tickets[i] - rides)
    return "%s %s" % (rides, promotions)

run()
#run(Pool(4))
