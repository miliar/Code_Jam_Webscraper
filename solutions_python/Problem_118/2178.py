#!/usr/bin/env python
import math

def convertToInts(aline):
    alist=aline.split(' ')
    therange=[ int(x) for x in alist ]
    return therange
 
if __name__ == "__main__":
    cases = input()
      
    for case in xrange(0, cases):
        therange = convertToInts(raw_input())
        counter=0
        for number in xrange(therange[0], therange[1]+1):
            if str(number)==(str(number))[::-1]: 
                root=math.sqrt(number)
                if root.is_integer() and str(int(root))==(str(int(root)))[::-1]:      
                    counter+=1
        print("Case #%i: %i" % (case+1, counter))
