import math
import sys

def isPerfectSquare(n):
    x = math.sqrt(n)
    return x == int(x)

def isPalindrome(s):
    if len(s) <= 1: return True
    return s[0] == s[-1] and isPalindrome(s[1:-1])
    

def run():
    t = int(raw_input())
    for x in range(t):
        a, b = raw_input().split(' ')
        count = 0
        for y in range(int(a), int(b)+1):
            if isPerfectSquare(y):
                if isPalindrome(str(y)) and isPalindrome(str(int(math.sqrt(y)))):
                    count += 1
        print 'Case #%d: %d' % (x + 1, count)
    return

if __name__ == "__main__":
    run()
    sys.exit(0)
    
