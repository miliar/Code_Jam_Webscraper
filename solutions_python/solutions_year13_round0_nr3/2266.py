#!/usr/bin/python
import sys
import math

def check_square(n):
	result = 0
	fairsqrt = int(math.sqrt(n))
	if math.pow(fairsqrt, 2) == float(n):
		result = int(math.sqrt(n))
	
	return result

def check_fair(n):
	sn = str(n)
	lsn = len(sn)
	result = True
	if n == 0:
		result = False
	if lsn > 1:
		for i in range(0, lsn/2):
			if sn[i] != sn[lsn - i - 1]:
				result = False
				break
	
	return result
		

def get_fairsquare(n, m):
	result = 0
	for i in range(n, m+1):
		if check_fair(i) and check_fair(check_square(i)):
			result += 1

	return result


fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

ntests = int(fin.readline().rstrip())

for i in range(0, ntests):
	(n, m) = fin.readline().rstrip().split()
	(n, m) = (int(n), int(m))
	result = get_fairsquare(n, m)

	fout.write("Case #" + str(i+1) + ": " + str(result) + "\n")

fin.close()
fout.close()

