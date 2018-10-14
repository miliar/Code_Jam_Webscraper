
import string
import re

def smallestNum(s):
    newS = ""
    copyS = s
    for j in range(0, len(s)):
        smallI = 0
        smallest = copyS[0]
        for i in range(0,len(copyS)):
            if(copyS[i] < copyS[smallI]):
                smallest = copyS[i]
                smallI = i

        if(smallI != len(copyS)-1):
            copyS = copyS[0:smallI] + copyS[smallI+1:]
        else:
            copyS = copyS[0:smallI]
        newS = newS + smallest
    return newS

def findNextNum(s):
    if len(s) == 1:
        return s+"0"
    
    count = 0
    smallest = 0
    for i in range(len(s)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if s[i] > s[j]:
                if smallest == 0 or int(s[0:j]+s[i]+smallestNum(s[j:i]+s[i+1:])) < smallest:
                    smallest = int(s[0:j]+s[i]+smallestNum(s[j:i]+s[i+1:]))


    if smallest != 0 :
        return smallest

    if s[len(s)-1] != "0":
        return s[len(s)-1]+"0"+smallestNum(s[0:-1])

    for i in range(len(s)-1,-1,-1):
        if s[i] != "0":            
            return s[i]+"0"+smallestNum(s[0:i]+s[i+1:])
    

s = raw_input()
numCases = int(s)

    
for i in range(numCases):
    s = raw_input()
    num = findNextNum(s)

    print "Case #{0}:".format(1+i), num
    

