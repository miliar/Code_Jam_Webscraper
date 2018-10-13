#!/usr/bin/python
"""Problem C. Fair and Square
   author: hkpeprah"""

def isPalindrome( n ):
    """Determines if a number n is a palindrome."""
    string = str(n)
    length = len(string)
    for indice in xrange(0, min(1, length / 2)):
        if not( string[indice] == string[length - indice - 1] ): 
            return False
    return True

if __name__ == "__main__":
    T = int(raw_input())
    for cases in xrange(1, T + 1):
        boundaries = (raw_input()).split()
        a, b = int(boundaries[0]), int(boundaries[1])
        square_and_fair, indice = 0, -1
        palindromeList = []
        for n in xrange(1, b + 1):
            if isPalindrome(n): 
                palindromeList.append(n)
                if indice == -1 and n >= a:
                    indice = len(palindromeList) - 1
        for i in xrange(indice, len(palindromeList)):
            sqr = pow(palindromeList[i], 0.5)
            for m in xrange(0, i + 1):
                if ( palindromeList[m] == sqr ):
                    square_and_fair += 1
                    break
        print "Case #%d: %d"%(cases, square_and_fair)
