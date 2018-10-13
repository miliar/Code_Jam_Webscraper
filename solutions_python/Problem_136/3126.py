import sys, itertools
from collections import namedtuple
from itertools import chain, cycle
from pprint import pprint
from decimal import Decimal

output_line = "Case #{X:d}: {time:.7f}"


if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            C, F, X = map(Decimal, inhandle.readline().split())

            rate = 2
            timetorate = 0
            besttime = X / rate
            while True:
                timetorate += C / rate
                rate += F
                thistime = timetorate + X / rate
                if thistime <= besttime:
                    besttime = thistime
                else:
                    break

            outline = output_line.format(X=t + 1, time=besttime)
            print(outline, file=outhandle)
            print(outline)
