#!/usr/bin/python

def calc(s, min, sup):
	avg = s / 3
	mod = s % 3

	if ( s ==0 and min >0):
		return 0

	if (mod == 0):

		if (avg >= min):
			return 1

		elif (sup > 0):
			if (avg + 1) >= min:
				return 2

	elif (mod == 1):

		if (avg >= min or (avg + 1) >= min):
			return 1

		elif (sup > 0):
			if (avg + 1) >= min:
				return 2

	elif (mod == 2):

		if (avg >= min or (avg + 1) >= min):
			return 1

		elif (sup > 0):
			if (avg + 2) >= min:
				return 2
	
	return 0;

def main():
	file_in = open("b.in", "r")
	file_out = open("b.out", "w")

	for i in xrange(int(file_in.readline())):
		line = file_in.readline()
		c = 0
		googlers = int(line.split()[0])
		sup = int(line.split()[1])
		p = int(line.split()[2])

		for k in xrange(0, googlers):
			s = int(line.split()[3 + k])
			
			ret = calc(s, p, sup) 
			if (ret == 1):
				c += 1
			elif (ret == 2):
				sup -= 1;
				c += 1

		file_out.write("Case #%s: %s\n" % (i + 1, c))

	file_in.close()
	file_out.close()

if __name__ == "__main__":
	main()
