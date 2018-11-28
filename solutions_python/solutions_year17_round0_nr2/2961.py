#!/usr/bin/env python

import fileinput
import math
import sys

if __name__ == "__main__":
    case = 0

    for line in fileinput.input():
        line = line.rstrip()

        if case == 0:
            T = int(line)
        elif case:
            N = int(line)
            S = str(N)
            L = len(S)

            # print(line, file=sys.stderr)
            # print("\t N %d" % N, file=sys.stderr)
            # print("\t L %d" % L, file=sys.stderr)

            D = L - 1
            while D > 0:
                # print("\t\t D %d" % D, file=sys.stderr)
                DL = int(S[D - 1])
                DR = int(S[D])
                # print("\t\t\t DL:DR %d:%d" % (DL, DR), file=sys.stderr)
                if DL > DR:
                    # print("\t\t\t\t fix", file=sys.stderr)
                    sub = int(S[D:]) + 1
                    # print("\t\t\t\t sub %d" % sub, file=sys.stderr)
                    N -= sub
                    S = str(N)
                D -= 1

            # print("\tCase #%d: %s" % (case, N), file=sys.stderr)
            print("Case #%d: %s" % (case, N))

        case += 1
