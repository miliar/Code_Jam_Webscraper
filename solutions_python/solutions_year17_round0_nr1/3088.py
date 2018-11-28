def toggle(p):
	if p == '-': return '+'
	return '-'

def pancakes(stack, size):
	n = len(stack)
	overlap = size*2 - n
	left = n - size
	right = n - size + overlap
	if not all(p == '-' for p in stack[left:right]) and not all(p == '+' for p in stack[left:right]):
		return "IMPOSSIBLE"

	flips = 0
	left = 0
	right = len(stack) - 1
	#print ''.join(stack)
	while (left < right):
		if stack[left] == '-':
			for i in range(left, left + size, 1):
				stack[i] = toggle(stack[i])
			flips += 1
		left += 1
		#print ''.join(stack)
		if stack[right] == '-':
			for i in range(right, right - size, -1):
				stack[i] = toggle(stack[i])
			flips += 1
		right -= 1
		#print ''.join(stack)
	#print ''.join(stack)
	if not all(p == '+' for p in stack):
		return "IMPOSSIBLE"

	return str(flips)
    
        
if __name__ == '__main__':
    for T in range(int(raw_input().strip())):
        stack, size = raw_input().strip().split()
        stack = [p for p in stack]
        size = int(size)
        print "Case #%d: %s" % (T+1, pancakes(stack, size))