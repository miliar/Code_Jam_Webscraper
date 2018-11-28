def solve(allStalls, guests):
	# return (startLocation, length)
	queue = []
	queue.append((0, allStalls - 1))

	while guests > 1:
		start, length = queue.pop(0)
		mid = start + length / 2
		if mid - 1 >= start:
			queue.append((start, mid - 1 - start))
		if mid + 1 <= start + length:
			queue.append((mid + 1, start + length - (mid + 1)))
		queue.sort(key=lambda tup: tup[0])
		queue.sort(key=lambda tup: tup[1], reverse=True)
		guests -= 1

	start, length = queue.pop(0)
	mid = start + length / 2
	end = start + length
	return (max(mid - start, end - mid), min(mid - start, end - mid))	

inFile = 'C-small-1-attempt1.in'
with open(inFile) as f:
    content = f.readlines()

content = [x.strip() for x in content]
nums = content[1:]

results = []
for num in nums:
	temp = num.split()
	stalls = temp[0]
	guests = temp[1]
	results.append(solve(int(stalls), int(guests)))

outFile = 'result'
with open(outFile, 'w') as f:
	for i in xrange(len(results)):
		line = ''
		if i == len(results) - 1:
			line = 'Case #%d: %d %d' % (i + 1, results[i][0], results[i][1])
		else:
			line = 'Case #%d: %d %d\n' % (i + 1, results[i][0], results[i][1])
		f.write(line)