import sys,string,heapq

def flip(cakes, s, e):
	flipped = ''
	for c in cakes[s:e]:
		if c == '+':
			flipped = flipped + '-'
		else:
			flipped = flipped + '+'
	return cakes[0:s] + flipped + cakes[e:]

def to_string(ls):
	output = ''
	i = 0
	while ls[i] == '0':
		i += 1
		if i >= len(ls):
			return '0'
	for c in ls[i:]:
		output = output + c
	return output

def aux(num):
	ls = [c for c in num]
	if len(num) < 2:
		return num
	for i in range(len(ls) - 1):
		prev = int(ls[i])
		curr = int(ls[i+1])
		if prev > curr:
			prev -= 1
			ls[i+1:] = ['9' for x in ls[i+1:]]
			ls[i] = str(prev)
	return to_string(ls)

def make():
	return []

def push(h, item):
	heapq.heappush(h, -1 * item)

def pop(h):
	return -1 * heapq.heappop(h)

def decide_case(case_str):
	case = case_str.strip().split()
	N = int(case[0])
	k = int(case[1])
	h = make()
	push(h, N)
	min = -1
	max = -1
	while k > 0:
		k -= 1
		interval = pop(h)
		if interval % 2 == 0:
			min = interval // 2 - 1
			max = interval // 2
		else:
			min = max = interval // 2
		if min > 0:
			push(h, min)
		if max > 0:
			push(h, max)

	return (max, min)

T = int(sys.stdin.readline())
n = 0
for line in sys.stdin:
	n += 1
	result = decide_case(line)
	print("Case #%d: %d %d" % (n, result[0], result[1]))