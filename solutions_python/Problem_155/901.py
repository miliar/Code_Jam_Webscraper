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
                cases = int(line)
            else:
                values = line.split(" ")
                public = values[1]
                nbFriend = 0
                ovationCount = 0
                for i in range(0,len(public)):
                    while not ovationCount >= i:
                        nbFriend += 1
                        ovationCount += 1
                    ovationCount += int(public[i])
                print("Case #{}: {}".format(count,nbFriend))

if __name__ == "__main__":
    main()
