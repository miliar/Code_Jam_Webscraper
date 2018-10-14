import sys


DEBUG=True if len(sys.argv) > 1 else False

def debug(*texts):
    if DEBUG:
        print("[DEBUG]", *texts, flush=True)



def flip(pk, start, end):
    for i in range(start, end):
        if pk[i] == '-':
            pk[i] = '+'
        else:
            pk[i] = '-'


def solve(pk, f):
    pk = list(pk)
    p = 0
    flips = 0
    while p <= len(pk) - f:
        debug(pk, p)
        if pk[p] == '-':
            flip(pk, p, p+f)
            flips += 1
        p += 1
    
    if '-' in pk:
        solution = "IMPOSSIBLE"
    else:
        solution = str(flips)

    return solution



for case in range(1, int(sys.stdin.readline())+1):
    pancakes, flipper = sys.stdin.readline().split()
    flipper = int(flipper)

    debug("pancakes: {0} ; flipper: {1}".format(pancakes,flipper))

    solution = solve(pancakes, flipper)

    print("Case #{0}: {1}".format(case, solution))

