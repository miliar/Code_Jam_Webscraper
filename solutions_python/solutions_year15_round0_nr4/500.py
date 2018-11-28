#!/usr/bin/python3
import re, sys, math

def main():
    with open(sys.argv[1]) as file:
        count = -1
        case = 0
        for line in file.readlines():
            line = line.rstrip("\n")
            count += 1
            if count == 0:
                pass
            else:
                val = [int(x) for x in line.split(" ")]
                X,R,C = val[0],val[1],val[2]
                if solve(X,R,C):
                    res = "GABRIEL"
                else:
                    res = "RICHARD"
                print("Case #{}: {}".format(count,res))

def solve(X,R,C):
    if X == 1:
        return True
    elif not R*C % X == 0:
        return False
    elif X > R and X > C:
        return False
    elif C > R:
        return solve(X,C,R)
    else:
        if X == 2:
            return True
        elif X == 3:
            if C == 1:
                return False
            else:
                return True
        elif X == 4:
            if C <= 2:
                return False
            else:
                return True


if __name__ == "__main__":
    main()
