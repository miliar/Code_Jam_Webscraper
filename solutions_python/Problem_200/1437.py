import sys,string

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

def decide_case(case_str):
	num = case_str.strip()
	prev = ''
	curr = aux(num)
	while curr != prev:
		prev = curr
		curr = aux(curr)
	return to_string(curr)

T = int(sys.stdin.readline())
n = 0
for line in sys.stdin:
	n += 1
	result = decide_case(line)
	print("Case #%d: %s" % (n, result))