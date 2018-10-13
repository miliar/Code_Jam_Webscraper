import math
import re

def isPalindrome(x):
	s1 = str(int(x))
	s2 = s1[::-1]
	return s1==s2

def isSquare(x):
  x = x
  seen = set([x])
  while x * x != x:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

T = input()
for testcase in range(1,T+1):
	line = raw_input().split();
	lo = int(line[0]);
	hi = int(line[1]);
	x = lo;
	count = 0;
	while x <= hi:
		if math.sqrt(x).is_integer():
			if isPalindrome(x) and isPalindrome(math.sqrt(x)):
				count += 1
		x+=1
	print "Case #"+str(testcase)+": "+str(count)