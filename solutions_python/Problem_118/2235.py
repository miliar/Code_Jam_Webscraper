import sys
import math
import pdb
def isPalindrome(n):
    return str(n) == str(n)[::-1]

T = int(sys.stdin.readline().strip())

for i in range(T):
    (A, B) = [int(j) for j in sys.stdin.readline().strip().split()]
    count = 0
    for n in range(A, B+1):
        if isPalindrome(n) :
            sqrt = int(math.sqrt(n))
            if sqrt*sqrt == n and isPalindrome(sqrt):
                count = count+1
    print "Case #" + str(i+1) + ":",
    print count
