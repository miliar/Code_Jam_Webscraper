#!/bin/env python3
#

import re


def main():
    input_file = "./A-large.in"
    output_file = "./result.txt"
    case_T = 0
    case_num = 0
    S = []

    with open(input_file, "r") as in_f, open(output_file, "w") as f:
        for line in in_f:
            if case_T == 0:
                case_T = int(line)
                print(case_T)
            else:
                case_num += 1
                Smax, S = line.split()
                audience = 0
                need_man = 0
#                print(Smax)
                for i in range(int(Smax)):
                    audience += int(S[i])
#                    print(i, S[i], S[i+1], audience)

                    if int(S[i+1]) != 0:
                        diff = int(i) + 1 - audience
                        if diff > 0:
                            need_man += diff
                            audience += diff
#                            print(i, need_man, diff)

                print(need_man)
                f.write("Case #{0}: {1}\n".format(case_num, need_man))


if __name__ == "__main__":
    main()
