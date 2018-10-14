#!/usr/bin/python

import sys

def can_fit(x, r, c):
    richard = {}

    richard['11'] = [1]
    richard['12'] = [1,2]
    richard['21'] = [1,2]
    richard['13'] = [1]
    richard['31'] = [1]
    richard['14'] = [1,2]
    richard['41'] = [1,2]
    richard['22'] = [1,2]
    richard['23'] = [1,2,3]
    richard['32'] = [1,2,3]
    richard['24'] = [1,2]
    richard['42'] = [1,2]
    richard['33'] = [1,3]
    richard['34'] = [1,2,3,4]
    richard['43'] = [1,2,3,4]
    richard['44'] = [1,2,4]

    return x in richard[str(r) + str(c)]

def main():
    test_cases = []
    with open(sys.argv[1], 'r') as f:
        for l in f:
            test_cases.append(l.strip())
    test_cases = filter(lambda t: len(t) != 2, test_cases)

    for i,t in enumerate(test_cases):
        x = int(t[0])
        r = int(t[2])
        c = int(t[4])
        print("Case #" + str(i+1) + ": " + ("GABRIEL" if can_fit(x,r,c) else "RICHARD"))

if __name__ == "__main__":
    main()
