
stack = []

def flip(pcks, i, k):
	o = pcks[:i]
	for j in range(i, i+k):
		o += "+" if pcks[j] == '-' else "-"
	return o+pcks[i+k:]

def isHappy(pcks):
	return "-" not in pcks

def process(size):
	(pcks, steps) = stack.pop(0)
	if isHappy(pcks):
		return steps

	for j in range(len(pcks) - size + 1):
		fpcks = flip(pcks, j, size)

		exist = False
		for s in stack:
			if s[0] ==fpcks:
				exist = True
				break

		if not exist:
			stack.append((fpcks, steps+1))

count = int(input())
for i in range(count):
	line = input()
	pcks = line.split()[0]
	size = int(line.split()[1])

	stack = []
	stack.append((pcks, 0))
	
	minCount = None
	while minCount == None and len(stack) > 0:
		minCount = process(size)
		
		if(stack and stack[len(stack)-1][1] > len(pcks) * size):
			minCount = "IMPOSSIBLE"
			break

		if len(stack) > 10:
			p1 = stack[:10]
			p1.sort(key=lambda a: a.count("+"))
			stack = p1 + stack[10:]

	print("Case #"+str(i+1)+": "+str(minCount))