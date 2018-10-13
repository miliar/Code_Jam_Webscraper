#!/usr/bin/python2

import math

# Take ints as args
def isPalindrome(a):
  if str(a) == str(a)[::-1]:
    return True
  else:
    return False

def isSquare(a):
  # To avoid float precision problems, I'll find the sqrt
  # and use the closes integer to find the square
  s = math.sqrt(a)

  if math.ceil(s)**2 == a or math.floor(s)**2 == a:
    return int(s) 
  else:
    return False

if __name__ == "__main__":

  f = open('sample', 'r')

  # Number of samples
  n = int(f.readline().replace('\n', ''))

  for i in range(n):
    
    # Read A and B
    l =  f.readline().replace('\n', '').split(' ')
    a = int(l[0])
    b = int(l[1])

    matches = 0

    for number in  range(a,b+1):

      #If number is a palindrome
      if isPalindrome(number):
        
        # Square?
        sr = isSquare(number)

        if sr != False:

          if isPalindrome(sr):

            #print "Number "+str(number)+" is fair and square! Square root: "+str(sr)
      
            matches = matches+1

    print "Case #"+str(i+1)+": "+str(matches)
