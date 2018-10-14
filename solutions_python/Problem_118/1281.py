from math import *
import random
import datetime

def roundUp(floating):
    """Rounds a float to upper int if it has a decimal"""
    if floating==int(floating):
        return int(floating)
    else:
        return int(round(floating+0.5))
    

def innerLimits(pair):
    """Round a float tuple pair inwards
Returns pair<int>"""
    return (roundUp(pair[0]),int(pair[1]))

def isPalindrome(string):
    """Checks whether string is a plaindrome"""
    if len(string) == 1:
        return True
    if len(string) == 2:
        return string[0]==string[1]
    return (string[0]==string[-1]) and isPalindrome(string[1:-1])
    


#-----------------Main------------------------
                             
def fs(filename = "fs.in"):
    txt = open(filename, "rU")
    solution = open("solution.txt","w")
    #Read topline info
    topline=txt.readline()
    noCases = int(topline.strip())


    SMALL=1000
    LARGE=10**14
    LARGE2=10**100

    limits= ( 1 , SMALL ) #WHICH DATASET


    #Squareness palindromes:
    squareLimits = ( sqrt(limits[0]), sqrt(limits[1]) ) #Floats
    trueLimits = innerLimits(squareLimits) #int sqrt limits rounded in

    lengthdata=(len(str(trueLimits[0]))/2.0 , len(str(trueLimits[1]))/2.0 )
    lengthCutPoint= (roundUp(lengthdata[0]),roundUp(lengthdata[1]))

    genLimits=( int( str(trueLimits[0])[:lengthCutPoint[0]]) ,
                int( str(trueLimits[1])[:lengthCutPoint[1]]) )

    #generate the palindromes
    fAndSquare=[]    
    for x in xrange( min(genLimits), max(genLimits)+1 ):

        
        #Case1 "asd"+"sa"
        if len(str(x)) == 1:
            test=x
        else:
            test= int( str(x) + str(x)[1::-1] )
        
        if (trueLimits[0] <= test) and (test <= trueLimits[1]) and (isPalindrome(str(test**2))):
            fAndSquare.append(test**2)


        #Case2 "asd"+"dsa"
        test= int( str(x) + str(x)[::-1] )
        if (trueLimits[0] <= test) and (test <= trueLimits[1]) and (isPalindrome(str(test**2)) ):
            fAndSquare.append(test**2)

    print fAndSquare


    

    
    #For each game:
    for case in range(1,noCases+1):
        caseSoln=0
        d = txt.readline().strip().split(" ") #Chews the line and array<str> it
        
        for element in fAndSquare:
            if (int(d[0]) <= element) and (element <= int(d[1])):
                caseSoln +=1
        
        solution.write("Case #"+str(case)+": " + str(caseSoln)+"\n")
        
    txt.close()
    solution.close()
    print "Done"

    
