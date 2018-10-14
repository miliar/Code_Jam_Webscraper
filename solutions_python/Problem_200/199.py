import sys
import math

def main():
    inputFile = open(sys.argv[1], "r")
    numCases = int(inputFile.readline())
    for n in range(1,numCases+1):
        s = inputFile.readline().strip()
        limits = []
        for i in range(len(s)):
            limits.append(int(s[i]))
        (number,base) = tidy(0,0,limits,False)
        print("Case #%i: %i"%(n,number))

def tidy(index,lastDigit,limits,noConstraint):
    if (index==len(limits)):
        return (0,1)
    if noConstraint:
        for digit in range(9,lastDigit-1,-1):
            (number,base) = tidy(index+1,digit,limits,noConstraint)
            if number!= -1:
                return (number+base*digit,base*10)
    else:
        for digit in range(limits[index],lastDigit-1,-1):
            if (digit!=limits[index]):
                (number,base) = tidy(index+1,digit,limits,True)
            else:
                (number,base) = tidy(index+1,digit,limits,False)
            if number != -1:
                return (number+base*digit,base*10)
    return (-1,-1)

main()