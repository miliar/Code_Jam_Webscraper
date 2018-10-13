def answer(number):
	add = 0
	index = 0
	total = 0
	for i in number:
		curr = int(i)
		if(index > total):
			add = add + index - total
			total = index
		total = total + curr
		index += 1
	return add

lines = [line.strip() for line in open('in')]
n = lines[0]

for x in range(int(n)):
	g = lines[x+1].split()[1]
	ans = answer(g)
	print('Case #' + str(x+1) + ': ' + str(ans))
