number = raw_input()

def parseInput(example):
	stripped_example = example.strip()
	return (int(stripped_example), [int(i) for i in example.strip()])

def solve(example):
	(number, listed_number) = parseInput(example)
	pos = -1
	for i in range(len(listed_number) - 1):
		if(listed_number[i] > listed_number[i + 1]):
			pos = i
			break
	if(pos == -1):
		return(example)
	new_num = listed_number[:pos] + [listed_number[pos] - 1] + [9]*(len(listed_number) - pos - 1)
	while new_num[0] == 0:
		new_num.pop(0)
		pass
	return(solve(''.join(map(str,new_num))))

for n in xrange(int(number)):
	example = raw_input()
	print "Case #" + str(n + 1) +": " + str(solve(example))