from sys import stdin


stdin.readline()
ti = 1
for line in stdin:
	arr = line.split()
	opposite = set()
	combine = {}
	i = 0
	C = int(arr[i])
	i += 1
	for j in xrange(i, i + C):
		combine[arr[j][:2]] = arr[j][2]
		combine[arr[j][1::-1]] = arr[j][2]
	i += C
	D = int(arr[i])
	i += 1
	for j in xrange(i, i + D):
		opposite.add(arr[j])
		opposite.add(arr[j][::-1])
	i += D
	N = int(arr[i])
	i += 1
	S = arr[i]
	stack = []
	for c in S:
		stack.append(c)
		while len(stack) >= 2:
			x = ''.join(stack[-1:-3:-1])
			if x in combine:
				stack.pop()				
				stack.pop()
				stack.append(combine[x])
			else:
				break
		for c2 in stack[:-1]:
			x = stack[-1] + c2
			if x in opposite:
				stack = []
				break
	print 'Case #' + str(ti) + ': [' + ', '.join(stack) + ']'
	ti += 1
			
			
		
				
		
	
		
	
	
