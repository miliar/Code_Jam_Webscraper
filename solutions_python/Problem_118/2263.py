import sys
import math
inp = sys.stdin.readlines()
cases = [(int(x), int(y)) for x, y in [l.split() for l in inp[1:]]]

def isPalindrome(s):
  if len(s) % 2:
    return s[:len(s)/2] == ''.join(reversed(s[len(s)/2+1:]))
  else:
    return s[:len(s)/2] == ''.join(reversed(s[len(s)/2:]))

for i, case in enumerate(cases):
  count = 0
  for j in range(case[0], case[1]+1):
    if isPalindrome(str(j)):
      if math.sqrt(j) == int(math.sqrt(j)) and isPalindrome(str(int(math.sqrt(j)))):
	count += 1
  print "Case #%d: %d" % (i+1, count)