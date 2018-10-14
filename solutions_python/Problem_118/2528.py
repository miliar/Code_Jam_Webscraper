# Tim Cohen
# fair and square


import sys

from math import sqrt

def  main():

    input_fn = sys.argv[1]
    input_fd = open( input_fn, 'r' )

    numberTestCases = int( input_fd.readline() ) 

    i = 1

    while ( i < ( numberTestCases + 1 ) ):

        bounds = input_fd.readline().split()
        A      = bounds[0]
        B      = bounds[1]

        fairAndSquare( i, A, B )

        i += 1


def fairAndSquare( testCase, A, B ):

    count = 0

    A = int(A)
    B = int(B)
    index = A

    while ( index <= B ):
        
        if ( isPalindrome( str(index) ) ):
            if isSquare( index ):
               if ( isPalindrome(str(int(sqrt(index))))):
                   count += 1

        index += 1

    print "Case #%s: %s" % ( testCase, count )

def isSquare( number ):
    
    root = sqrt(number)
    
    if ( root % 1 ):
        return False
    else:
        return True

def isPalindrome( number ):
    
    numberList = []

    for digit in number:
        numberList.append( digit )

    length = len( numberList )


    halfway = length / 2
    
    i = 0
    
    while ( i < halfway ):
        if ( numberList[i] != numberList[length-i-1] ):
            return False
        i += 1


    return True
        

if __name__ == '__main__':
    main()
