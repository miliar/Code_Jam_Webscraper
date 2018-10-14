#!/usr/bin/python3

import sys

def flip(string, start, size):
    for i in range(start, start+size):
        if(string[i] == '-'):
            string[i] = '+'
        else:
            string[i] = '-'

def solve(testCase):
    string = testCase[0]
    size = testCase[1]
    flips = 0
    #First pass
    if '-' in string:
        for i in range(len(string) - size + 1):
            if string[i] == '-':
                flip(string, i, size)
                flips += 1
    else:
       return flips 

    #2nd Pass
    if '-' in string:
        for i in range(len(string) - size + 1):
            if string[i] == '-':
                flip(string, i, size)
                flips += 1
    else:
       return flips 

    #Final check
    if '-' in string:
        return "Impossible"
    else:
        return flips 

def main():
    filename = sys.argv[1]
    lines = []
    numTests = 0

    with open(filename) as f:
        lines = f.readlines()

    numTests = int(lines[0])
    lines.pop(0)

    for i in range(numTests):
        lines[i] = lines[i].split(" ")
        lines[i][0] = list(lines[i][0])
        lines[i][1] = int(lines[i][1])
    
    #----------------
    count = 1
    for testCase in lines:
        print("Case #" + str(count) + ": " + str(solve(testCase)))
        count += 1


if __name__ == '__main__':
    main()
