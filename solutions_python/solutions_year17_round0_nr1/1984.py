# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import string
import sys

def minFlips(s,lenS,k):
  flag = True
  for i in s:
    if i == '0':
      flag = False
      break
  if flag == True:
    return 0

  numFlips = 0
  
  for pos in range(lenS-k+1):
    if s[pos] == '0':
      numFlips+=1
      s = modify(s,pos,k,lenS)

  flag = True
  for i in s:
    if i == '0':
      flag = False
      break
  if flag == True:
    return numFlips
  
  return "IMPOSSIBLE"

def modify(s, i, k,lenS):
  if i == 0:
    a = string.replace( s[:k], "0", "2")
    a = string.replace( a, "1", "0")
    a = string.replace( a, "2", "1")
    return a + s[k:]

  elif i == lenS-k:
    a = string.replace( s[-k:], "0", "2")
    a = string.replace( a, "1", "0")
    a = string.replace( a, "2", "1")
    return s[:-k] + a
  else:
    a = string.replace( s[i:i+k], "0", "2")
    a = string.replace( a, "1", "0")
    a = string.replace( a, "2", "1")    
    return s[:i] + a + s[i+k:]

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s, k = [u for u in raw_input().split(" ")]  # read a list of integers, 2 in this case
  k = int(k)
  s = string.replace(string.replace(s, "+", "1"), "-", "0")
  mF = minFlips(s, len(s), k)
  
  print "Case #{}: {}".format(i, mF)
  # check out .format's specification for more formatting options
