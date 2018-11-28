#!/bin/env python3
#

import os


def main():
    input_file = "./D-small-attempt0.in"
    output_file = "./result-{0}".format(os.path.basename(input_file))
    case_T = 0
    case_num = 0
    winner = ""

    with open(input_file, "r") as in_f, open(output_file, "w") as f:
        for line in in_f:
            if case_T == 0:
                case_T = int(line)
                winner = ""
                print(case_T)
            else:
                case_num += 1
                X, R, C = [int(x) for x in line.split()]

                grid = R * C
                print(X, R, C, grid)

                if grid % X == 0:
                    if X > 2 and X < 7:
                        if C > R:
                            shouter = R
                        else:
                            shouter = C

                        if X - shouter >= 2:
                            winner = "RICHARD"
                            print("a")
                        else:
                            winner = "GABRIEL"
                            print("b")
                    elif X >= 7:
                        winner = "RICHARD"
                        print("e")
                    else:
                        winner = "GABRIEL"
                        print("c")
                else:
                    winner = "RICHARD"
                    print("d")

                f.write("Case #{0}: {1}\n".format(case_num, winner))


if __name__ == "__main__":
    main()
