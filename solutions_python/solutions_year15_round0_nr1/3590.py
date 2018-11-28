#!/usr/bin/env python2
import sys

def str_to_aud(string):

    aud = []

    for i in range(int(string[0]) + 1):
        aud.append(int(string[2 + i]))

    return aud

def friends_needed(aud):

    stoodup = 0;
    needed = 0;

    for i in range(len(aud)):

        if i > stoodup and aud[i] != 0:
            diff = (i-stoodup)
            stoodup = stoodup + diff + aud[i]
            needed = needed + diff
            continue;

        stoodup = stoodup + aud[i];

    return needed

def main():
    #sys.argv[1] is the file
    f = open(sys.argv[1], 'r')
    testcases = int(f.readline())

    for i in range(testcases):
        needed = friends_needed(str_to_aud(f.readline()))
        print("Case #{0}: {1}".format(i+1, needed))


if __name__ == "__main__":
    main()
