import sys

def lastIndex(mylist, element):
	return len(mylist) - mylist[::-1].index(element) - 1

def reverseSignal(signal):
	if(signal == '-'): return '+'
	return '-'

def doFlip(mylist, k_size):
	for i in range(k_size):
		mylist[i] = reverseSignal(mylist[i])

num_args = int(sys.stdin.readline())

for case_number in range(0, num_args):
	line = sys.stdin.readline()
	if '\n' in line: line.replace('\n', '')
	line = line.split()

	pancakes = list(line[0])
	k_size = int(line[1])
	
	if '-' in pancakes:
		pancakes = pancakes[pancakes.index('-'):lastIndex(pancakes, '-') + 1]
	else:
		pancakes = []
	
	count = 0
	while len(pancakes) >= k_size:
		count += 1
		doFlip(pancakes, k_size)
		if '-' in pancakes:
			pancakes = pancakes[pancakes.index('-'):]
		else:
			pancakes = []

	if len(pancakes) == 0:
		print("Case #" + str(case_number + 1) + ": " + str(count))
	else:
		print("Case #" + str(case_number + 1) + ": " + "IMPOSSIBLE")



