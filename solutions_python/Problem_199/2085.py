testfile = open('A-large.in', 'r')
outputfile = open('flipout.txt', 'w')

def last_k_happy(stack, k):
	for i in range(k):
		if(stack[-1-i] == '-'):
			return False
	return True

def flip_next_k(stack, start, k):
	for i in range(k):
		if stack[start + i] == '-':
			stack[start + i] = '+'
		else:
			stack[start + i] = '-'

def process_stack(stack, k):
	stack_length = len(stack)
	flip_count = 0
	for i in range(stack_length - k + 1):
		if(stack[i] == '-'):
			flip_next_k(stack, i, k)
			flip_count += 1
	return flip_count if last_k_happy(stack, k) else 'IMPOSSIBLE'

num_test_cases = int(testfile.readline().strip())
for i in range(num_test_cases):
	line = testfile.readline().strip().split()
	# treat string as array since python strings are immutable
	stack_string = list(line[0])
	k = int(line[1])
	(x, y) = (i + 1, process_stack(stack_string, k))
	outputfile.write('Case #' + str(x) + ': ' + str(y))
	if(i + 1 < num_test_cases):
		outputfile.write('\n')