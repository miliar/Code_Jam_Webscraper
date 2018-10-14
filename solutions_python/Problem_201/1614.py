import os
import math

with open("c.in", "r+") as f:
	lines = [x.strip() for x in f.readlines()]

answ = ""

for case in range(1, int(lines[0]) + 1):
	n = int(lines[case].split(" ")[0])
	k = int(lines[case].split(" ")[1])

	level = math.floor(math.log(k, 2))

	if (level == 0) :
		answ += "Case #{0}: {1} {2}\n".format(case, int(n/2), int((n-1)/2))
	else :
		nodes = (2**level)
		n -= nodes - 1
		
		num1 = int(n / nodes)		
		num2 = num1 + 1
		qty2 = n - (num1 * nodes)
		qty1 = nodes - qty2

		k -= nodes - 1

		if k <= qty2:
			answ += "Case #{0}: {1} {2}\n".format(case, int(num2/2), int((num2-1)/2))	
		else :
			answ += "Case #{0}: {1} {2}\n".format(case, int(num1/2), int((num1-1)/2))	

			



with open("c.out", "w") as f:
	f.write(answ)
