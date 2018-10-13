from sys import argv
from math import sqrt

def is_square(number):
	if number == 1: return True

	x = number // 2
	seen = set([x])
	while x * x != number:
		x = (x + (number // x)) // 2
		if x in seen: return False
		seen.add(x)
	return True

script, rname, wname = argv

infile = open(rname)
outfile = open(wname, 'w')

tc = int(infile.readline())

for i in range(1,tc+1):
	answer = 0;
	a, b = map(int,infile.readline().split(' '))
	
	for num in range(a, b+1):
		if is_square(num) and str(num) == str(num)[::-1]:
			s = str(int(sqrt(num)))
			if s == s[::-1]:
				answer += 1

	print("Case #%d: %d" % (i, answer))
	outfile.write("Case #%d: %d\n" % (i, answer))