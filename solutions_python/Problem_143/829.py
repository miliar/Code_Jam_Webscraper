#!/usr/bin/env python3
import argparse
import math
import logging



def read_input():
    f = open(args.inputfile)
    T = int(f.readline())
    for i in range(T):
        yield [int(i) for i in f.readline().split()]


def output(n, s):
    outstring = "Case #{}: {}\n".format(n, s)
    print(outstring, end="")
    outfile.write(outstring)


def solve(A, B, K):
    logging.debug("solving {} {} {} \n\n".format(A,B,K))
    logging.debug(A & B)

    count = 0
    for i in range(A):
        for j in range(B):
            logging.debug("<{},{}> = {}".format(i,j, i&j))
            if i & j < K:
                count += 1


    # logging.debug([bin(i).split('b')[1] for i in range(A)])
    # logging.debug([bin(i).split('b')[1] for i in range(B)])

    return count



def main():
    for n, case in enumerate(read_input(), start=1):
        logging.info(case)
        A, B, K = case
        answer = solve(A, B, K)
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            input("anserwing {}, look OK?".format(answer))
        output(n, answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="google code jam practice")
    parser.add_argument("inputfile", type=str, help="input file")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    outfile = open(args.inputfile + ".out", "w")
    if args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
        logging.debug("Verbose debuging mode activated")
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    main()
