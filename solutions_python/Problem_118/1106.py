import math

def iffair(num):
	chars = list(str(num))
	mid = int(math.floor(len(chars) / 2))
	for i in range(0, mid):
		if chars[i] != chars[len(chars)-i-1]:
			return False
	return True

def judge_all(filename):
	f = open(filename)
	lines = f.readlines()
	f.close

	num = int(lines[0])
	for i in range(1, num + 1):
		count = 0
		o_start = int(lines[i].split()[0])
		o_end = int(lines[i].split()[1])
		start = int(math.ceil(math.sqrt(o_start)))
		end = int(math.floor(math.sqrt(o_end)))
		for k in range(start, end + 1):
			if iffair(k):
				if(iffair(k*k)):
					count += 1
		phrase = str(count)
		print "Case #" + str(i) +": " + phrase

judge_all("C-small-attempt0.in")