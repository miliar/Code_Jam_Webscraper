#! /usr/bin/env python

import sys
def is_palindrome(s):
	y = s[::-1]
	if (y == s):
		return True
	else:
		return False

def is_square(apositiveint):
	if apositiveint == 1:
		return (True, 1)
	x = apositiveint // 2
	seen = set([x])
	while x * x != apositiveint:
		x = (x + (apositiveint // x)) // 2
		if x in seen: return (False, 0)
		seen.add(x)
	return (True, x)



	


F = open(sys.argv[1], "r");
OUT = open(sys.argv[2], "w");




NumOfTests = F.readline();
CaseNum = 1
for line in F:
	line = line.split()
	lower = float(line[0])
	upper = float(line[1])
	count = 0
	while(lower <= upper):
		(isSquare, num) = is_square(lower);
		if isSquare:
			if is_palindrome(str(int(num))):
				if is_palindrome(str(int(lower))):
					count = count + 1
		lower = lower + 1
	OUT.write("Case #%d: %d\n" % (CaseNum, count))
	CaseNum = CaseNum + 1
