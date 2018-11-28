import sys
import numpy as np
import math

file = sys.argv[1]
print(file)


def main():
    count = 0
    case = 0
    with open(file, 'r') as i:
        with open(file + " out", 'w') as o:
            for i, line in enumerate(i):
                if i > 0:
                    if count == 0:
                        case += 1
                        d, n = [int(c) for c in line.strip().split(" ")]
                        horses = []
                    count += 1
                    horses.append([int(c) for c in line.strip().split(" ")])
                    if count == n + 1:
                        o.write("Case #{}: {}\n".format(case, prog(horses)))
                        count = 0
                    """
                    new = int(line.strip())
                    """

def prog(arg):
    print(arg)
    final = arg[0][0]
    n = arg[0][1]

    slowest = None
    for x in range(1, len(arg)):
        w = (final - arg[x][0]) / arg[x][1]
        if slowest is None or w > slowest:
            slowest = w

    return final / slowest

if __name__ == "__main__":
    main()
