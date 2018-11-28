#-------------------------------------------------------------------------------
# Name:        Problem A. Standing Ovation
# Purpose:     Code Jam Qualification Round 2015
#
# Author:      Vihanga Liyanage
#
# Created:     11/04/2015
# Copyright:   (c) Vihanga Liyanage 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    infile = open("input.txt", "r")
    outfile = open("output.txt", "w")
    T = int(infile.readline()) #test cases
    for i in range(T):
        (max, lst) = (x for x in infile.readline().split())
        max = int(max)
        count = 0
        result = 0
        for j in range(len(lst)):
            if int(lst[j]) != 0:
                count += int(lst[j])
            else:
                while count < j+1:
                    result += 1
                    count += 1
        outfile.write("Case #" + str(i+1) + ": " + str(result) +"\n")

if __name__ == '__main__':
    main()
