#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="google code jam bullseye")
parser.add_argument("inputfile", type=str, help="input file")
args = parser.parse_args()
outfile = open(args.inputfile + ".out", "w")

# 1 ml covers pi cm^2

def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        r , t = (int(i) for i in f.readline().split())
        yield r,t


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)

def paint_for_ring(r):
    return 2*r+1


def main():
    used = 0

    for n, case in enumerate(read_input(), start=1):
        print(case)
        r, t = case
        paint_used = 0
        rings = 0;
        while True:
            paint_used += paint_for_ring(r)
            if(paint_used > t):
                break
            rings +=1
            r+=2
        # print(paint_for_ring(r))
        print(rings, paint_used)
        output(n, rings)


if __name__ == "__main__":
    main()
