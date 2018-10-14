#!/usr/bin/python

fin = open('3in')
fout = open('3out', 'w')
lines = fin.read().strip().split('\n')[1:]
for index, line in enumerate(lines):
	nums = line.split()
	a = int(nums[0]) 
	b = int(nums[1]) 
	out = 0
	seen = []
	for i in range(a, b + 1):
		stri = str(i)
		for cnt in range(1, len(stri)):
			recycled = stri[-cnt:] + stri[:-cnt]
			recycled = int(recycled)
			if recycled > i and recycled <= b:
				if (i, recycled) not in seen:
					seen.append((i, recycled))
					out += 1

	fout.write("Case #%d: %d\n"%(index + 1, out))
			
