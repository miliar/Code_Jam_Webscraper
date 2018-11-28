import fileinput
from functools import reduce

def isTidy(N):
    if len(N) == 1:
        return True
    for i in range(0, len(N)-1):
        if int(N[i]) > int(N[i+1]):
            return False
    return True

def reorder(a, b):
    a = int(a)
    b = int(b)
    a -= 1
    b = 9
    return str(a) + str(b)


def solve(N):
    while not isTidy(N):
        for i in range(0, len(N)):
            if int(N[i]) > int(N[i+1]):
                result = reorder(N[i], N[i+1])
                N = N = N[:i] + result + '9'*(len(N)-(i+2))
                break
    return N.lstrip('0')


f = fileinput.input()
T = int(f.readline())
for case in range(1, T+1):
    N = f.readline().split()[0]
    solution = solve(N)
    print("Case #{0}: {1}".format(case, solution))
