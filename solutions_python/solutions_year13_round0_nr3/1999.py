#!/usr/bin/python
import sys
import math
import time

def checkPalindrome(num):
  l = len(num)
  flag = True
  for i in range(0, l/2+1):
    if num[i] != num[l-i-1]:
      flag = False
      return flag
  return flag      

if __name__ == "__main__":
  #start = time.time()
  inputFile = file("C-small-attempt0.in", 'r')
  cases = (int)(inputFile.readline())
  output = []
  temp = cases
  while(cases > 0):
    count = 0
    line = inputFile.readline()
    intBegin = int(line.split()[0])
    intEnd = int(line.split()[1])
    begin = int(math.ceil(math.sqrt(intBegin)))
    end = int(math.floor(math.sqrt(intEnd)))
    for i in range(begin, end+1):
      if(checkPalindrome(str(i))):
        if(checkPalindrome(str(i**2))):
	  count = count+1
    data = "Case #"+str(temp-cases+1)+": "+str(count)
    output.append(data)
    cases = cases - 1
  for i in output:
    print i
