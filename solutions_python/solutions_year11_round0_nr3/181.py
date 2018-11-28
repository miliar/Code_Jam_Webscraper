import sys
import re

def xorlist(list):
    lenl = len(list)
    if lenl < 0:
        return 0
    result = list[0]
    for i in range(1,lenl):
        result = result ^ list[i]
    return result

def addlist(list):
    lenl = len(list)
    if lenl < 0:
        return 0
    result = list[0]
    for i in range(1,lenl):
        result += list[i]
    return result

def main():
    infile = open(sys.argv[1])
    T = int(infile.readline().strip())

    for i in range(0, T):
        infile.readline()
        N = [int(o) for o in infile.readline().strip().split()]
        if xorlist(N) != 0:
            print "Case #" + str(i+1) + ": NO"
            continue
        N.sort()
        N.reverse()
        N.pop()
        print "Case #" + str(i+1) + ": " + str(addlist(N))

if __name__ == "__main__":
    main()
