# -*- coding: utf-8 -*-
"""
Google Code Jam 2009
Qualification C
Welcome to Code Jam
"""

# --- constants ---
BaseStr = "welcome to code jam"
BaseDict = dict()
for l in BaseStr:
  if BaseDict.has_key(l):
    BaseDict[l] += 1
  else:
    BaseDict[l] = 1
BaseLen = len(BaseStr)

# --- modules ---
import sys

# --- funcs ---
def filter(testcase):
  valuable_str = ""
  f_dict = dict()
  for i in range(len(testcase)):
    if testcase[i] == BaseStr[0]:
      break
  teststr = testcase[i:]
  for key in BaseDict:
    f_dict[key] = 0
  prev = "@"
  for c in teststr:
    if f_dict.has_key(c):
      if prev != c:
        f_dict[c] += 1
      valuable_str += c
    prev = c
  for key in BaseDict:
    if f_dict[key] < BaseDict[key]:
      return ""
  return valuable_str

def calc(teststr,nb):
  v_str = filter(teststr)
  if v_str == "":
    return 0
  vlen = len(v_str)
  b = 0
  sum = 1
  retsum = 0
  count = 0
  prev = 0
  for i in range(vlen):
    if v_str[i] == BaseStr[b]:
      count += 1
    elif (b+1 < BaseLen and v_str[i] == BaseStr[b+1]):# or b+1 == BaseLen:
      if b > nb:
        for j in range(i+1,vlen):
          if v_str[j] == BaseStr[b]:
            if BaseLen-b <= vlen - j:
              v_seq = v_str[0:prev] + v_str[j:]
              #print v_str,"|",v_seq,nb,b
              retsum += calc(v_seq,b)
              retsum %= 10000
            
      b += 1
      prev = i
      sum *= count
      sum %= 10000
      count = 1
      #if b == BaseLen-1:
      #  break
    
      
  if b < BaseLen-1:
    sum = 0
  sum *= count
  sum %= 10000
  #print v_str,sum,BaseStr[nb]
  retsum += sum
  retsum %= 10000
  return retsum
      


# --- main ---
# the number of test cases
line = sys.stdin.readline().rstrip("\n")
N = int(line)

for n in range(N):
  # test case
  line = sys.stdin.readline().rstrip("\n")
  ans = calc(line,-1)
  ansstr = "%04d"%(ans)
  print "Case #"+str(n+1)+":",ansstr
