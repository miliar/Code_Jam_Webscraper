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
        N = int(f.readline())
        yield N


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)


def tidy_int(l):
    return sum(i*(10**power) for power,i in enumerate((l)))



def tidy_gen(N):
    l = [0]
    while tidy_int < N:
        if len(l) == 1:
            l[0] += 1
            yield l



def istidy(i):
    print(i)
    s = str(i)
    l = [int(s) for s in str(i)]
    def ordered(head, lst):
        # print("ordered called ", head, lst)
        if len(lst) > 0:
            if head > lst[0]:
                return False
            return ordered(lst[0], lst[1:])
        return True
    return ordered(l[0], l[1:])


def solve(N):
    for i in range(N,1,-1):
        # print(i)
        if istidy(i):
            return i
    return 1

def main():
    for n, case in enumerate(read_input(), start=1):

        answer = solve(case)

        output(n, answer)


if __name__ == "__main__":
    main()
