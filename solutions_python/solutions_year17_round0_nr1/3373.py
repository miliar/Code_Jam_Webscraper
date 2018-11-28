#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="google code jam pancake")
parser.add_argument("inputfile", type=str, help="input file")
args = parser.parse_args()
outfile = open(args.inputfile + ".out", "w")


def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        cakes, K = f.readline().split(" ")
        yield list(cakes), int(K)


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)

def flip(s):
    flipmap = {'-': '+', '+': '-'}
    return flipmap[s]

def solve(cakes, K):
    #print(cakes, K)
    flipcount = 0
    for i in range(len(cakes)):
        if cakes[i] == '-':
            if i+K > len(cakes):
                return "Impossible"
            flipcount += 1
            for j in range(K):
                cakes[i+j] = flip(cakes[i+j])
            #print(cakes)
    return flipcount

def main():
    for n, case in enumerate(read_input(), start=1):

        answer = solve(*case)

        output(n, answer)


if __name__ == "__main__":
    main()
