import itertools

fd = open("in1.in", "r")

lines = fd.readlines()

testcases = int(lines[0])

fout = open("out1", "w")

def flip(pancake):
	if(pancake=='-'):
		return '+'
	else:
		return '-'


def flip_pancakes(data, start, end):
	result = list(data)
	for i in xrange(start, end):
		result[i] = flip(result[i])
	return result

for line_ind in xrange(1,len(lines)):
	line  = lines[line_ind]
	words = line.split()
	pancakes = words[0]
	k = int(words[1])
	fout.write("Case #" + str(line_ind) + ": ")

	# Your code here
	cnt = 0
	i = 0
	flag = True
	while(1):
		try:
			index = pancakes.index('-')
		except :
			break
		cnt += 1
		if((index <= i and i > 0) or index + k > len(pancakes)):
			print index, i, k
			flag = False
			break
		i = index 
		pancakes = flip_pancakes(pancakes, i, i+k)

	if(flag):
		fout.write(str(cnt))
	else:
		fout.write("IMPOSSIBLE")
	fout.write("\n")