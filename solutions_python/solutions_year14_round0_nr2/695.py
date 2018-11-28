#!/usr/bin/python
import sys

def calc_new(costs, production, target, intermediate, farms):
    intermediate = intermediate + costs/(production*farms + 2)
    total = intermediate + target/(production*(farms+1)+2)
    return intermediate, total

def main():
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[1][:-2] + "out", "w")

    for case in range(1, int(infile.readline())+1):
        costs, production, target = (float(i) for i in infile.readline().split())

        old_time = sys.float_info.max
        new_time = target/2
        farms = 0
        intermediate = 0

        while new_time < old_time:
            old_time = new_time

            intermediate, new_time = calc_new(costs, production, target, intermediate, farms)
            farms += 1

        print("Case #{0}: {1}".format(case, old_time), file=outfile)

if __name__ == "__main__":
        main()
