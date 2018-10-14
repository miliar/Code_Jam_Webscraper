#-------------------------------------------------------------------------------
# Name:        Fair and Square
# Purpose:
#
# Author:      udonko
#
# Created:     14/04/2013
# Copyright:   (c) udonko 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import sys
from math import sqrt
def checkTxt(text):
    flag = True
    for i in range(len(text)/2):
        if text[i] != text[len(text)-1-i]:
            flag = False
            break
    return flag
def resolve(a,b):
    count = 0
    root = int(sqrt(a))
    while(True):
        square = root* root
        if a <= square <= b :
            text2 = str(root)
            flag2 = checkTxt(text2)
            if flag2 == True:
                text1 = str(square)
                flag1 = checkTxt(text1)

                if flag1 == True:
                    count += 1
                    #sys.stdout.write(str(root)+" "+str(square)+"\n")
        if square > b:
            break
        root += 1
    return count
def main():
    infile = open("input.txt","r")
    outfile = open("output.txt","w")
    num = int(infile.readline())

    # num of test loop
    for i in range(num):
        #sys.stdout.write(str(i)+"----\n")
        temp = infile.readline()
        temps = temp.split()
        a = int(temps[0])
        b = int(temps[1])

        #resolve
        ret = resolve(a,b)
        outfile.write("Case #"+str(i+1)+": "+str(ret)+"\n")



    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()