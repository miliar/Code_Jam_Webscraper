from itertools import islice
import sys

def solve(S):
    i = 0
    invited = 0
    clapping = 0
    for Si, NSi in enumerate(S):
        if NSi > 0:
            if Si == 0 or clapping >= Si:
                clapping += NSi
                invited += 0
            elif Si > 0:
                invited += Si - clapping
                clapping += Si - clapping + NSi
    return invited

def main():
    inp = iter(sys.stdin)
    T = int(next(inp))
    for x, line in enumerate(islice(inp, 0, T), start=1):
        line = line.split(" ", 1)
        Smax = int(line[0], 10)
        S = [int(i) for i in line[1][:Smax + 1]]
        N = solve(S)
        print "Case #{0}: {1}".format(x, N)

if __name__ == "__main__":
    main()
