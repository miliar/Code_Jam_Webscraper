from math import sqrt
from math import ceil
from math import floor


def isPalindrome(number):

    numstr=str(number)
    retval=True
    i=0
    length=len(numstr)

    while (i<=length/2):
        if numstr[i]!=numstr[-i-1]:
            retval=False
            break
        i+=1


    return retval

def FairAndSquare(fname):

    infile=open(fname,"r")
    outfile=open(fname+".out","wb")
    
    numcases=int(infile.readline())

    for i in range(numcases):
        l,u=[int(x) for x in infile.readline().split()]
        candidates=range(int(ceil(sqrt(l))),int(floor(sqrt(u)))+1)

        answer=0

        for candidate in candidates:
            if (isPalindrome(candidate)==True):
                if (isPalindrome(candidate*candidate)):
                    answer+=1
        outfile.write("Case #"+str(i+1)+": "+str(answer)+"\n")

    infile.close()
    outfile.close()            
    
