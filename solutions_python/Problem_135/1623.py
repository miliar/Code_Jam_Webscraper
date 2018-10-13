#!/usr/bin/python

from sys import stdin

def main():
    numsamples = int(stdin.readline())
    for i in range(1, numsamples + 1):
        ans = readpuzzle()
        print "Case #%d: %s" % (i, str(ans))

def readpuzzle():
    first = int(stdin.readline())
    for i in range(1, 5):
        line = stdin.readline().strip()
        if i == first:
            possible = line.split(" ")
    second = int(stdin.readline())
    for j in range(1,5):
        line = stdin.readline().strip()
        if j == second:
            also_possible = line.split(" ")
    matches = []
    for num in possible:
        if num in also_possible:
            matches.append(num)
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        return "Bad magician!"
    else:
        return "Volunteer cheated!" 

if __name__ == "__main__":
    main()
