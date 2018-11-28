import sys
import math


def IsPalindrome(s, i):
	if (i < 10):
		return True;
	return(s == s[::-1])

f = open(sys.argv[1])
lines = f.readlines()
f.close()

i = 1
t = int(lines[0])

for tt in range(t):
	count = 0
	line = lines[i]
	i += 1
	range1 = line.split()
	if len(range1) < 2:
		break;
	(start, end) = range1
	start_float = math.sqrt(int(start))
	if (start_float - int(start_float) < 0.000001):
		start1 = int(start_float)
	else:
		start1 = int(start_float) + 1
	end1 = int(math.sqrt(int(end)))+1
	#print(str(start1) + ":" + str(end1))

	for num in range(start1, end1):
		if IsPalindrome(str(num), num) and IsPalindrome(str(num*num), num*num):
			#print (str(num) + " " + str(num*num))
			count += 1

	print ("Case #" + str(i-1) + ": " + str(count))
