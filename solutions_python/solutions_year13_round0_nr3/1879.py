# fairAndSquare.py

from math import sqrt

def isPalindrome(a):
    return str(a)==str(a)[::-1]

def fairAndSquare(a,b):
    n = int(sqrt(a))

    total=0
    finalsqrt=sqrt(b)

    if n**2 < a:
        n+=1

    while n<=finalsqrt:
        if isPalindrome(n) and isPalindrome(n*n):
            total+=1
        n+=1
    return total

def main():
    outlist = []

    n = raw_input()
    for m in range(int(n)):
        (a,b) = map(int,raw_input().split())
        
        outlist.append(fairAndSquare(a,b))
    
    for (pos,a) in enumerate(outlist):
        print "Case #%d: %d"%(pos+1,a)
        
if __name__ == "__main__":
    main()
