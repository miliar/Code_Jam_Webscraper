import math
from decimal import *
__author__ = 'Mad Cow'

def FairAndSquare(path):
    with open(path, 'r') as f:
        case = 1
        output = ''
        n_cases = int(f.readline().strip())
        for i in range(n_cases):
            nm = f.readline().strip().split(' ')
            lower = Decimal(nm[0])
            upper = Decimal(nm[1])
            output += "Case #" + str(case) + ": " + str(Judge(lower, upper))
            if case < n_cases:
                output += '\n'
            case += 1
    with open ('FairAndSquare.out', 'w') as f:
        f.write(output)


def Judge(lower, upper):
    rl = int(math.ceil(float(lower.sqrt())))
    ru = int(upper.sqrt())
    count = 0;
    for i in range(rl, ru + 1):
        count += JudgeAux(i)
    return count

def JudgeAux(i):
    if not str(i) == str(i)[::-1]:
        return 0
    t = Decimal(i) * Decimal(i)
    if not str(t) == str(t)[::-1]:
        return 0
    return 1

FairAndSquare('C-small-attempt0.in')


