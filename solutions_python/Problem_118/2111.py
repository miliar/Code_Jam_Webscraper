import os
import math


PALENDROMES = {}

def is_palendrome(value):
    if value in PALENDROMES:
        return PALENDROMES[value]
    valstr = str(value)
    ret = valstr == valstr[::-1]
    PALENDROMES[value] = ret
    return ret

def count(lower, upper):
    min = int(math.ceil(math.sqrt(lower)))
    max = math.sqrt(upper)
    if math.ceil(max) != max:
        max = math.floor(max)
    max = int(max)
    count = 0
    for i in range(min, max + 1):
        if is_palendrome(i) and is_palendrome(i * i):
            count += 1
    return count


def solve(filename):
    with open(filename) as data:
        first = True
        case = 1
        for line in data:
            line = line.strip()
            if not line: continue
            if first:
                first = False
            else:
                lower, upper = map(int, line.split(' '))
                print("Case #{case}: {out}".format(case=case, out=count(lower, upper)))
                case += 1

if __name__ == "__main__":
    filename = "C-small-attempt0.in"
    fname = os.path.join(os.path.dirname(__file__), "data", filename)
    solve(fname)

