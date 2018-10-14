#! /usr/bin/env python3

import os
import os.path
import argparse
from pprint import pprint

def solve(N, R, O, Y, G, B, V):
    # With O, G and V, only possible sequences are:
    # BOBOB, RGRGR, YVYVYV
    if O > B or G > R or V > Y:
        return "IMPOSSIBLE"

    if R == G and N == R+G:
        print("Special case RG")
        return "RG" * G
    if O == B and N == O+B:
        print("Special case BO")
        return "BO" * B
    if V == Y and N == Y+V:
        print("Special case YV, N={}".format(N))
        return "YV" * V

    special = {}
    if G > 0:
        special["R"] = "RG" * G + "R"
        R -= G
        N -= 2*G
    if O > 0:
        special["B"] = "BO" * O + "B"
        B -= O
        N -= 2*O
    if V > 0:
        special["Y"] = "YV" * V + "Y"
        Y -= V
        N -= 2*V

    result = ""
    values = [["R", R], ["Y", Y], ["B", B]]
    last = ''

    while N > 0:
        values.sort(key=lambda x: x[1], reverse=True)
        assert(values[0][1] > 0)
        index = 0
        first_char = values[index][0]

        if first_char == last:
            print("Can't use first")
            index = 1
        if values[index][1] == 0:
            return "IMPOSSIBLE"

        if N <= 3 and len(result) > 0 and result[0] != last:
            print("Fixing termination, result[0]={}, last={}".format(result[0], last))
            for i in range(3):
                if values[i][0] == result[0] and values[i][1] != 0:
                    index = i
                    break

        last = values[index][0]
        if last in special:
            result += special[last]
            del special[last]
        else:
            result += values[index][0]

        values[index][1] -= 1
        N -= 1
        print("{} {}={} {}={} {}={}".format(result, values[0][0], values[0][1], values[1][0], values[1][1], values[2][0], values[2][1]))

    if len(result) == 0 or result[0] == result[-1]:
        return "IMPOSSIBLE"

    return result

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help='Filename')

    args = parser.parse_args()

    outputfile = os.path.splitext(args.filename)[0] + ".out"

    with open(args.filename, 'r') as f:
        with open(outputfile, 'w+') as fout:
            num_tests = int(f.readline().strip())
            for testcase in range(1,num_tests+1):
                N, R, O, Y, G, B, V = [int(x) for x in f.readline().split(" ")]
                print("Case #{} Input: num={} R={} O={} Y={} G={} B={} V={}".format(testcase, N, R, O, Y, G, B, V))
                result = solve(N, R, O, Y, G, B, V)
                print("Output: {}".format(result))
                fout.write("Case #{}: {}\n".format(testcase, result))


