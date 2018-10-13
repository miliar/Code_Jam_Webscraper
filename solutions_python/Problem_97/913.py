import re

def rotatelist(l, i):
	if len(l) < 2:
		return l
	i = i % len(l)

	return l[i:] + l[:i]

def choosetwo(size):
	if size == 0 or size == 1:
		return 0
	return size * (size - 1) / 2

def recycledNumbers(a, b, dig):
	if dig < 2:
		return 0

	result = 0;
	digs = [1]
	for i in range(1, dig):
		tens = digs[i - 1] * 10
		digs.append(tens)
	ib = int(b)
	for i in range(int(a), int(b) + 1):
		once = 1
		summ = i
		test = []
		for j in range(1, dig):
			#n = rotatelist(list(str(i)), j)
			#ni = int(''.join(n))
			ni = (i / digs[j]) + ((i % digs[j]) * digs[dig - j])
			if (ni < int(a)) or ni > ib:
				continue
			#if we have handled this number, just skip
			if ni < i:
				once = 0
				break

			if summ % ni != 0:
				summ = summ * ni
				test.append(ni)
				once = once + 1

		result = result + choosetwo(once) #choosetwo(len(mark))		
	return result

def debug(a, b, dig):
	if dig < 2:
		return 0
	mark = {}
	min = 1
	for i in range(dig - 1):
		min = min * 10
	result = 0;
	digs = [1]
	for i in range(1, dig):
		tens = digs[i - 1] * 10
		digs.append(tens)
	ib = int(b)
	for i in range(int(a), int(b) + 1):
		summ = i
		for j in range(1, dig):
			#n = rotatelist(list(str(i)), j)
			#ni = int(''.join(n))
			ni = (i / digs[j]) + ((i % digs[j]) * digs[dig - j])
			#if (i == 1202):
			#	print ni
			if (ni < min) or ni > ib or ni < i:
				continue

			if summ % ni != 0:
				summ = summ * ni
				mark[str(i) + " " + str(ni)] = 1

	print len(mark)
	mkey = mark.keys()
	#print mkey
	for i in range(len(mkey)):
		print mkey[i]
	#print mark.keys()
	#return mark


def recycle(filepath):
	f = open(filepath, 'r+')
	infile = re.split('in', filepath)
	outfile = infile[0] + "out"
	print outfile
	o = open(outfile, "w+")
	#number of test cases
	t = int(f.readline())
	i = 1
	for line in f:
		sl = re.split(" ", line)
		result = recycledNumbers(sl[0], sl[1], len(sl[0]))
		buf = "Case #" + str(i) + ": " + str(result)
		i = i + 1
		print buf
		o.write(buf + '\n')
	f.close()
	o.close()

#print recycledNumbers("100", "500", 3)
#print debug("1111", "2222", 4)
#print recycledNumbers("1111", "2222", 4)
#recycle("./C-small-test.in")
recycle("./C-small-attempt1.in")

#print recycledNumbers("11111", "22222", 5)
#print recycledNumbers("1000000", "2000000", 7)
