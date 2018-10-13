import sys
import math

def isPalindrome(x):
    x = str(x)
    length = len(x)
    
    for i in range(length):
        if x[i] != x[length - i - 1]:
            return False

    return True

def processCase():
    A, B = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    nbFairAndSquare = 0
    
    for x in range(int(math.ceil(math.sqrt(A))), int(math.floor(math.sqrt(B))) + 1):
        if isPalindrome(x) and isPalindrome(x ** 2):
            nbFairAndSquare += 1
    return nbFairAndSquare

def main():
    T = int(sys.stdin.readline())
    for i in range(T):
        result = processCase()
        print 'Case #%d: %d' % (i + 1, result)
        
if __name__ == '__main__':
    main()
