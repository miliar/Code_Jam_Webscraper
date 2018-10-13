#!/usr/bin/env python3
import sys

def main(argv):
    if len(argv) != 2:
        print("Usage : {} input".format(argv[0]))
        return -1

    with open(argv[1]) as infile:
        nb_tests = int(infile.readline())

        #lets read the input!
        for t in range(nb_tests):
            test = []
            for i in range(2):
                row_num = int(infile.readline())
                for r in range(1,4+1):
                    if r == row_num:
                        test.append([int(e) for e in infile.readline().split()])
                    else:
                        infile.readline()

            inter = set(test[0]).intersection(set(test[1]))
            if len(inter) == 1:
                print("Case #{}: {}".format(t+1, list(inter)[0]))
            elif len(inter) > 1:
                print("Case #{}: Bad magician!".format(t+1))
            else:
                print("Case #{}: Volunteer cheated!".format(t+1))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
