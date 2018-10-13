#!/usr/bin/env python

import sys

def main():

    case = 1
    inputfile = open(sys.argv[1])
    outfile = open("output.txt", "w")
    inputfile.next()  # Skip number of cases
    fmt_str = "Case #%s: %.7f\n"

    for line in inputfile:
        total = 0.0
        rate = 2.0
        C, F, X = line.split()
        C = float(C)
        F = float(F)
        X = float(X)

        if X <= C:
            total = X / rate
            outfile.write(fmt_str % (case, total))
            case += 1
            continue

        while True:
            if (X / rate) < ((C / rate) + (X / (rate + F))):
                total += X / rate
                break
            total += C / rate
            rate = rate + F

        outfile.write(fmt_str % (case, total))
        case += 1

if __name__ == "__main__":
    main()
