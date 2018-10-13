number = raw_input()

switcher = {'+':'-', '-':'+'}

def switch(pos, string, size):
	for i in range(pos, pos + size):
		string[i] = switcher[string[i]]

def getTouple(example):
	l = example.split(" ")
	return(l[0], l[1])

def check(example):
	return '-' in example

def solve(example):
	(string, size) = getTouple(example)
	size = int(size)
	string = list(string)
	count = 0
	for i in xrange(len(string) - size + 1):
		if(string[i] == '-'):
			switch(i, string, size)
			count += 1
	if check(string):
		return 'IMPOSSIBLE'
	return count


for n in xrange(int(number)):
	example = raw_input()
	print "Case #" + str(n + 1) +": " + str(solve(example))