#!/usr/bin/env python
from __future__ import print_function

def main():
    f = open('myfile','w')
    with open("sample.txt") as fp:
        line_count = int(next(fp).strip())
        for inst in range(line_count):
            line = next(fp).strip()
            shyMax, audi = line.split()
            sum = 0
            pplcnt = 0
            for i in range(int(shyMax) + 1):
                if i > sum:
                    pplcnt += 1
                    sum += 1
                sum += int(audi[i])
            print("Case #{}: {}".format(inst + 1, pplcnt), file=f)

if __name__ == "__main__":
    main()
