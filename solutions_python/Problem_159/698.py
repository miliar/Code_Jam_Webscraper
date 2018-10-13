#-------------------------------------------------------------------------------
# Name:        Problem A. Mushroom Monster
# Purpose:     Code Jam 2015 - Round 1A 2015
#
# Author:      Vihanga Liyanage
#
# Created:     18/04/2015
# Copyright:   (c) Vihanga Liyanage 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
rate = 0

def one(lst):
    global rate
    tmpRate = 0
    result = 0
    for i in range (len(lst)-1):
        temp = lst[i+1] - lst[i]

        if temp < 0:
           result +=temp
           tmpRate = min(temp, tmpRate)
    rate = -tmpRate
    return -result

def two(lst):
    global rate
    result = 0
    for i in range (len(lst)-1):
        temp = lst[i]
        if temp > rate:
            result += rate
        else:
            result += temp
    print(result)
    return result

def main():
    infile = open("input.txt", "r")
    outfile = open("output.txt", "w")
    T = int(infile.readline()) #test cases
    for j in range(T):
        infile.readline()
        lst = [int(i) for i in infile.readline().split()]

        outfile.write("Case #" + str(j+1) + ": " + str(one(lst)) + " " + str(two(lst)) +"\n")


if __name__ == '__main__':
    main()
