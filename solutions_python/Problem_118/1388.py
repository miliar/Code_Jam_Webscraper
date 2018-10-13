#!/usr/bin/env python


import sys
import math

def findSquarePalindromes(low,high):
  #first, lets find all the palindromes between low and high, because that's going to vary a lot more
  #then, we'll check if each palindrome is a square
  #then, we'll check if the square root is a palindrome
  count = 0
  cur = findFirstPalindrome(str(low))
  while int(cur) <= high:
    if isSquare(int(cur)):
      count+=1
    cur=findNextPalindrome(cur)
  return count

def isSquare(cur): # using Newton's method (should be faster than binary search)
  guess = int(math.sqrt(cur))
  old_guess = -1
  while old_guess != guess:
    old_guess = guess
    guess = old_guess - (old_guess**2-cur)/(2*old_guess)
  if guess**2 == cur:
    return isPalindrome(guess)
  elif (guess+1)**2 == cur:
    return isPalindrome(guess+1)
  else:
    return False

def isPalindrome(num):
  snum=str(num)
  odd_digits=len(snum)%2
  first_digits=len(snum)/2
  return snum[:first_digits][::-1]==snum[first_digits+odd_digits:]

def findFirstPalindrome(low):
  odd_digits=len(low)%2
  first_digits=len(low)/2
  try:
    cur_backend = int(low[first_digits+odd_digits:])
    new_backend = int(low[:first_digits][::-1])
  except ValueError:
    cur_backend = 0
    new_backend = 0
  if cur_backend > new_backend:
    return findNextPalindrome(low)
  if odd_digits:
    new_first = low[:first_digits+1]
    return new_first+new_first[::-1][1:]
  else:
    new_first = low[:first_digits]
    return new_first+new_first[::-1]

def findNextPalindrome(low):
  odd_digits=len(low)%2
  first_digits=len(low)/2
  if odd_digits:
    new_first = str(int(low[:first_digits+1])+1)
    return new_first+new_first[::-1][1:]
  else:
    new_first = str(int(low[:first_digits])+1)
    if len(new_first)>first_digits: # if we rolled over to odd
      return new_first+new_first[::-1][1:]
    else:
      return new_first+new_first[::-1]

with open(sys.argv[1],'r') as f:
  t = int(f.readline())
  for z in range(t):
    low_endpoint,high_endpoint=map(int,f.readline().split())
    count = findSquarePalindromes(low_endpoint,high_endpoint)
    print "Case #%d: %d"%(z+1,count)
