#!/usr/bin/python
import os, sys, math

def fairnsquare(n):
  r = math.sqrt(n)
  if r != math.floor(r):
    return False
  if not palindrome(n) or not palindrome(int(r)):
    return False
  return True

def palindrome(n):
  s = str(n)
  for i in range(int(math.ceil(len(s) / 2))):
    if s[i] != s[len(s)-1-i]:
      return False
  return True

cases = int(raw_input())

for i in range(cases):
  ab = raw_input().split(" ")
  a = int(ab[0])
  b = int(ab[1])
  total = 0
  for j in range(a, b+1):
    if fairnsquare(j):
      total += 1
  print "Case #" + str(i+1) + ": " + str(total)
