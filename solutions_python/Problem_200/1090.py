import sys


DEBUG=True if len(sys.argv) > 1 else False

def debug(*texts):
    if DEBUG:
        print("[DEBUG]", *texts, flush=True)



def solve(n):
    for pos in range(len(n)-1, 0, -1):
        if n[pos-1] > n[pos]:
            for i in range(pos, len(n)):
                n[i] = '9'
            n[pos-1] = str(int(n[pos-1])-1)

    sol = int(''.join(n))

    return sol



for case in range(1, int(sys.stdin.readline())+1):
    number = sys.stdin.readline()
    number = list(number[:-1])

    debug("number:", number)

    solution = solve(number)

    print("Case #{0}: {1}".format(case, solution))

