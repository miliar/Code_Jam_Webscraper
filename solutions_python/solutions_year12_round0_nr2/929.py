import re

def dance(filepath):
	f = open(filepath, 'r+')
	infile = re.split('in', filepath)
	outfile = infile[0] + "out"
	print outfile
	o = open(outfile, "w+")
	#number of test cases
	t = int(f.readline())
	result = 0
	i = 1
	for line in f:
		sl = re.split(" ", line)
		n = int(sl[0])
		s = int(sl[1])
		p = int(sl[2])
		#print "Case #" + str(i) + ": number=" + sl[0] + " surprises=" + sl[1] + " point=" + sl[2]
		for index in range(3, len(sl)):
			level = ispossible(int(sl[index]), p)
			print level
			if level == 0:
				result = result + 1
			elif level == 1: 
				if s > 0:
					s = s - 1
					result = result + 1
		buf = "Case #" + str(i) + ": " + str(result)
		print buf
		o.write(buf + '\n')
		result = 0
		i = i + 1
	return result

def ispossible(tolpoints, p):
	"whether it possible to get a best score of p"
	rest = tolpoints - p
	if rest < 0:
		return 2
	#he can get the best score without surprise
	if (rest > 2 * p - 3):
		return 0
	#he can get the best score with a surprise
	elif (rest >= 2 * p - 4):
		return 1
	#no, you can't
	else:
		return 2

print dance("./B-small-attempt1.in")
print dance("./B-small-test.in")
print dance("./B-large.in")