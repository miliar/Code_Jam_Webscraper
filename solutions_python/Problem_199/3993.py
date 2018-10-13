def single_flip(pancake):
	if (pancake == "+"):
		return "-"
	if (pancake == "-"):
		return "+"

def flip(input, size, start):
	a = list(input)
	for i in xrange(start, start+size):
		a[i] = single_flip(a[i])
	return ''.join(a)

def all_flips(input, size):
	a = set()
	for i in xrange(len(input) - size + 1):
		a.add(flip(input, size, i))
	return a

def flipper(input, size):
	target = "+" * len(input)
	visited = set()
	queue = []
	queue.append([input])
	while (queue):
		path = queue.pop(0)
		node = path[-1]
		if node not in visited:
			# print(node)
			visited.add(node)
			if node == target:
				return path
			for adjacent in all_flips(node, size):
				new_path = list(path)
				new_path.append(adjacent)
				queue.append(new_path)
				# print(new_path)
		# print(path)
			# print(queue)
	return None

def runner(input, size):
	ans = flipper(input, size)
	if ans == None:
		return "IMPOSSIBLE"
	else:
		return str(len(ans) - 1)
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
inputs = list()
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  inputs.append((int(m), n))
for num, i in enumerate(inputs):
	size = i[0]
	input = i[1]
	print("Case #" + str(num + 1) + ": " + runner(input, size))