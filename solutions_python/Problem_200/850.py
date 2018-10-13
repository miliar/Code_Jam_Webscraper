#!/usr/bin/python

import sys


def solveTidy(n):
    n = str(n)
    l = 0
    o = ""
    last = 9
    for c in n[::-1]:
        if int(c)>last:
            last = int(c)-1
            o = str(last)+"9"*len(o)
        else:
            last = int(c)
            o = c+o
    return int(o)

def main():
    f = open("input.txt")
    numTests = int(f.readline())
    output = ""
    for i in range(numTests):
        n = f.readline()
        n = int(n)

        answer = solveTidy(n)
        output += "Case #" + str(i+1) + ": " + str(answer) + '\n'

    fout = open("output.txt", "w")
    fout.write(output)

if __name__ == "__main__":
    main()

