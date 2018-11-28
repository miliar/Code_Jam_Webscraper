def flip(element):
	if element == '+':
		return '-'
	else:
		return '+'

file = open("read.txt", 'r')
wfile = open("write.txt", 'w')
x = int(file.readline());
for mv in xrange(x):
	num, k = (file.readline().strip().split())
	num = list(num)
	k = int(k)
	start, end = 0, len(num) - 1
	#print num
	count = 0
	while (end >= start):
		for x in xrange(start, end + 1):
			if num[x] == '-':
				if x + k <= len(num):
					count += 1
					for y in xrange(x, x + k):
						num[y] = flip(num[y])
					start = x + 1
					break
				else:
					start = end + 1
					break
			start += 1
		#print start,end,num
		if end < start:
			break
		for x in xrange(end, start - 1, -1):
			if num[x] == '-':
				if x - k >= -1:
					count += 1
					for y in xrange(x, x - k, -1):
						num[y] = flip(num[y])
					end = x - 1
					break
				else:
					end = start - 1
					break
			end -= 1
		#print start,end,num
	imp = False
	for ele in num:
		if ele == '-':
			imp = True
			break
	if imp:
		print "IMPOSSIBLE"
		wfile.write("Case #" + str(mv + 1) + ": " + "IMPOSSIBLE")
	else:
		print mv,count
		wfile.write("Case #" + str(mv + 1) + ": " + str(count))
	wfile.write("\n")
	print "\n----\n"
	