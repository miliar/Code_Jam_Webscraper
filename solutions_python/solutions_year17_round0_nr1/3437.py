def solve(cakes, k):		
	count = 0
	for i in xrange(len(cakes)):
		if cakes[i] == '-' and i + k <= len(cakes):
			count += 1
			flip(cakes, i , i + k)
	if allHappy(cakes[len(cakes) - k:]) or allBlank(cakes[len(cakes) - k:]):
		return count
	else:
		return -1

def flip(cakes, start, end):
	for i in xrange(start, end):
		if cakes[i] == '+':
			cakes[i] = '-'
		else:
			cakes[i] = '+'

def allHappy(cakes):
	for cake in cakes:
		if cake == '-':
			return False
	return True
		
def allBlank(cakes):
	for cake in cakes:
		if cake == '+':
			return False
	return True

inFile = 'A-large.in'
with open(inFile) as f:
    content = f.readlines()

content = [x.strip() for x in content]
nums = content[1:]

results = []
for n in nums:
	cakes = list(n.split()[0])
	k = int(n.split()[1])
	res = solve(cakes, k)
	results.append(res)

print results

outFile = 'result'
with open(outFile, 'w') as f:
	for i in xrange(len(results)):
		if results[i] == -1:
			line = 'Case #%d: %s\n' % (i + 1, 'IMPOSSIBLE')
			f.write(line)
		else:
			line = 'Case #%d: %d\n' % (i + 1, results[i])
			f.write(line)



