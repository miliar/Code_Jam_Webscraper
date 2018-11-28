
import math

def ispal(s):
	return s == s[::-1]

def is_sqr(i):
	root = math.sqrt(i)
	if int(root + 0.5) ** 2 == i:
		return True
	return False

inf = open("3.dat")
test_case_count = int(inf.readline())

def handle(case_count,lo,hi):
	good_count = 0
	for i in range(lo,hi+1):
		if not ispal(str(i)):
			continue
		if not is_sqr(i):
			continue
		i_s = int(math.sqrt(i))
		if not ispal(str(i_s)):
			continue
		good_count = good_count + 1
		# print i, math.sqrt(i), is_sqr(i), i_s

	print "Case #%s: %s" % (case_count, good_count)

case_count = 1
while True:
	line = inf.readline().strip()
	
	if line is None:
		break
	if len(line)==0:
		break

	data = line.split()
	low = int(data[0])
	hi = int(data[1])	
	
	handle(case_count,low,hi)
	case_count = case_count + 1

