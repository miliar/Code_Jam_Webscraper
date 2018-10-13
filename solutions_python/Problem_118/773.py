#!/usr/bin/env python3
import argparse
import math

parser = argparse.ArgumentParser(description="google code jam practice all your base")
parser.add_argument("inputfile", type=str, help="input file")
args = parser.parse_args()
outfile = open(args.inputfile + ".out", "w")

def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        A, B = (int(i) for i in f.readline().split(" "))
        yield A, B


def output(n, s):
    outstring = "Case #{}: {}\n".format(n+1, s)
    print(outstring, end="")
    outfile.write(outstring)

def ispalendrome(N):
    s = str(N)
    for i,j in zip(s,reversed(s)):
        if i != j:
            return False
    return True

def isqrt(N):
    return int(math.sqrt(N))

def generate_palendromes(start, end):
    i = start
    done = False
    while not done:
        si = str(i)

        half_inc = math.ceil(len(si)/2)
        half_ex = math.floor(len(si)/2)
        prefix = si[0:half_inc]
        postfix = si[0:half_ex][::-1]
        i+=10**half_ex

        newpal = int(''.join((prefix, postfix)))
        if(newpal <= end):
            yield newpal
        else:
            done = True

def main():
    for n,case in enumerate(read_input()):
        A, B = case
        count = 0
        # print(list(generate_palendromes(15, 24)))
        # print(list(generate_palendromes(14, 24)))
        for i in generate_palendromes(isqrt(A), isqrt(B)+1):
            squared = i*i
            if(squared < A or squared > B):
                continue
            if(ispalendrome(squared)):
                count +=1

        output(n, count)

if __name__ == "__main__":
    main()
