import sys,string

def flip(cakes, s, e):
	flipped = ''
	for c in cakes[s:e]:
		if c == '+':
			flipped = flipped + '-'
		else:
			flipped = flipped + '+'
	return cakes[0:s] + flipped + cakes[e:]

def decide_case(case_str):
	words = case_str.split()
	pancakes = words[0]
	flipper = int(words[1])
	num_moves = 0
	prev = -1
	impossible = False
	while '-' in pancakes :
		i = min(pancakes.index('-'), len(pancakes) - flipper)
		if i == prev:
			impossible = True
			break
		pancakes = flip(pancakes, i, i+flipper)
		num_moves += 1
		prev = i
	if impossible:
		return -1
	else:
		return num_moves


T = int(sys.stdin.readline())
n = 0
for line in sys.stdin:
	n += 1
	result = decide_case(line)
	if result == -1:
		print("Case #%d: IMPOSSIBLE" % n)
	else:	
		print("Case #%d: %d" % (n, result))