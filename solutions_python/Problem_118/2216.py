#!/usr/bin/env python3 
import math

def ispalindrome(i):
    s = str(i)
    return s == s[::-1]
    
def solve(A,B):
    a = math.ceil(math.sqrt(A))
    b = math.ceil(math.sqrt(B+1))

    count = 0
    for y in range(a,b):
        x = y * y
        if ispalindrome(y) and ispalindrome(x):
#            print("%d ** 2 = %d" % (y,x))
            count = count + 1
    return count
            

if __name__ == "__main__":
    T = int(input())
    for c in range(T):
        [A,B] = [int(x) for x in input().split()]
        print("Case #%d: %d" % (c+1,solve(A,B)))
