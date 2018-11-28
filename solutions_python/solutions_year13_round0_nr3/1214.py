import sys
import string
import math


raw_input = input

def isPalindrome(n):

  sn = str(n)

  i = 0
  j = len(sn) -1

  while i < j:
      if sn[i] != sn[j]:
          return False
      i = i + 1
      j = j - 1
  return True
      



if __name__ == '__main__':
    
    nCases = int(raw_input())

    for nC in range(nCases):
        a, b = map(int, raw_input().split())

        sA = int(math.ceil(math.sqrt(a)))
        sB = int(math.floor(math.sqrt(b)))
        
        count = 0
        for n in range(sA, sB+1):
          nn = n*n
          if isPalindrome(n) and isPalindrome(nn):
              
              count += 1

        print("Case #%d: %d" % (nC+1, count)) 

