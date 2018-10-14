# Problem C. Fair and Square
# by gvaf

import sys

def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

def isPalindrome(num):
  n1 = str(num)
  n2 = n1[::-1]
  return (n1 == n2)
  
numTests = int(sys.stdin.readline())

for test in range(0, numTests):
  line = sys.stdin.readline().rstrip()
  numbers = line.split()
  a = int(numbers[0])
  b = int(numbers[1])
  start = find_invpow(a, 2)
  end   = find_invpow(b, 2) + 1
  numFair = 0

  x = start
  while( x <= end ):
     x2 = x * x
     if( x2 >= a and x2 <= b):
        if( isPalindrome(x) ):      
           if( isPalindrome(x2) ):
              numFair = numFair + 1
#              print( "isfair: %d x %d = %d" % (x,x,x2) ) 
     x = x + 1

  print("Case #%d: %d" % (test+1, numFair) )
