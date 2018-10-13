#!/usr/bin/python
import sys
import math
import gmpy # http://code.google.com/p/gmpy/

goodDigits = '14695'
#A palindrome cannot end with digit 0 in base 10.
#A square number can end only with digits 0, 1, 4, 6, 9, or 25 in base 10,

def main():
    f = open(sys.argv[1], 'rU')
    t = int(f.readline())

    fout = open(sys.argv[1]+'.out', 'w')

    for case in range(1,t+1):
        A, B = [int(x) for x in f.readline().split()]
        result = processcase(A,B)
        fout.write("Case #%(case)d: " %{"case":case})
        if result:
            fout.write(str(result))
        else:
            fout.write("0")
        fout.write("\n")

    fout.close()
    f.close()


def processcase(A,B):
    return sum(1 for _ in filter(palindromeQ,range(A,B+1)))
            

def palindromeQ(n):
    s = str(n)
    if s[-1] not in goodDigits:
        return False
    else:
        if gmpy.is_square(n):
            return (palindrome(s) and palindrome(str(math.floor(math.sqrt(n)))))
        else:
            return False
        
        

def palindrome(s):
    for i in range(len(s)//2):
        if (s[i] != s[-i-1]):
            return False
    return True


if __name__ == '__main__':
    main()

