import sys

def concat_str(args):
    s = ""
    for arg in args:
        s += str(arg)
    return s

def debug(*args):
    sys.stderr.write(concat_str(args) + "\n")

def printf(*args):
    debug(*args)
    print concat_str(args)

def int_input():
    return map(int, raw_input().split(' '))


#######################################################

P = 1000002013

def read_input():
    N, M = int_input()
    pairs = [int_input() for i in range(M)]
    return N, pairs

def cost(N, dist):
    return (dist * N) - ((dist * (dist - 1)) / 2) % P

def pair_cost(p, N):
    return (p[2] * cost(N, p[1] - p[0])) % P

def solve_connected(N, pairs):
    if pairs == []:
        return 0

    s = 0
    begin = [[e, 0, n] for e, o, n in pairs]
    end = [[o, 1, n] for e, o, n in pairs]

    events = begin + end
    events.sort()

    cards = []

    for pos, isend, n in events:
        if isend == 0:
            cards.append([pos, n])
        else:
            while n > 0:
                c = cards[-1]
                leaving = min(n, c[1])
                n -= leaving
                c[1] -= leaving
                s += leaving * cost(N, pos - c[0])
                if c[1] == 0:
                    cards.pop()

    if cards != []:
        debug("cards ISN'T EMPTY")

    return s % P
def solve(N, pairs):
    pairs.sort()

    s = 0
    maxi_end = 0
    current_pairs = []
    for p in pairs:
        if p[0] > maxi_end:
            s += solve_connected(N, current_pairs)
            current_pairs = []
        maxi_end = max(maxi_end, p[1])
        current_pairs.append(p)

    s += solve_connected(N, current_pairs)

    s2 = sum(map(lambda p: pair_cost(p, N), pairs))

    debug("cheated cost:", s)
    debug("regular cost:", s2)

    return (s2 - s) % P



#######################################################


for n_test_case in range(1, int(raw_input()) + 1):
    debug("Solving case ", n_test_case)

    printf("Case #", n_test_case, ": ", str(solve(*read_input())))

