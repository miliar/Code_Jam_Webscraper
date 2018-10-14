#!/usr/bin/env python

import sys

def list2int(li):
    return int(''.join(map(str,li)))

def check(number):
    last = 0
    for n in str(number):
        if int(n) < last:
            return False

        last = int(n)
    return True

def dec(number):
    if check(number):
        return number

    strnum = list(map(int, str(number)))

    last = strnum[-1]
    for i,v in reversed(list(enumerate(strnum))):
        if v > last:
            strnum[i] = v - 1
            for j in range(i + 1, len(strnum)):
                strnum[j] = 9
            return list2int(strnum)

        last = v

    return list2int(strnum)

def solve(number):
    while not check(number):
        number = dec(number)

    return number

def main(infile):
    with open(infile, 'r') as f:
        T = f.readline()

        case = 1
        for line in f:
            n = solve(int(line.rstrip()))
            print("Case #{}: {}".format(case, n))
            case = case + 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
