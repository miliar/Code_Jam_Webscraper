#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kirodh
#
# Created:     08/04/2017
# Copyright:   (c) kirodh 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from __future__ import print_function
def main():
    pass

if __name__ == '__main__':
    main()

nameoffile = "B-large.in"
outputfile = "output1.txt"
infile = open(nameoffile,"r")
outfile = open(outputfile,"w")

numcases = int(infile.readline())
for i in range(1,numcases+1):

    number = list(infile.readline()) # get rid of the newline char
    if number[len(number)-1] == "\n": number = number[0:-1]


    if len(number) == 1:
        print("Case #"+str(i)+": "+str(number[0]),file=outfile)
    else:
        constructednumber = ''
        tempcount = 1
        tempchar = ''
        for j in range(1,len(number)):
            if number[j-1] == number[j]:
                tempchar = number[j-1]
                tempcount += 1
            elif number[j-1] > number[j]:
                #subtract 1
                #print(tempchar)
                newchar = str(int(number[j-1])-1)
                #print(newchar)
                constructednumber = constructednumber + newchar
                constructednumber = constructednumber +"9"*(tempcount-1 + len(number[j:len(number)]))
                print("Case #"+str(i)+": "+str(int(constructednumber)),file=outfile)
                break
            else:
                constructednumber = constructednumber + tempcount*number[j-1]
                tempcount=1
                tempchar = ''
            if j==len(number)-1:
                constructednumber = constructednumber + tempcount*number[j]
                print("Case #"+str(i)+": "+str(int(constructednumber)),file=outfile)
infile.close()
outfile.close()


