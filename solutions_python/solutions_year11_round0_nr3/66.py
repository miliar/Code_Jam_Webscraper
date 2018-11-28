fin = open('in.txt','r')
fout = open('out.txt', 'w')
line = fin.readline().strip()
count = int(line)
for i in range(count):
	fin.readline()
	line = fin.readline().strip()
	#print line
	words = line.split(' ')
	arr = []
	for j in range(len(words)):
		arr.append(int(words[j]))
	arr.sort()
	flag = False
	ret = 0
	sum = 0
	for j in range(len(arr)):
		ret = 0
		sum = 0
		for k in range(len(arr)):
			if k != j:
				sum += int(arr[k])
				ret ^= int(arr[k])
		if ret == int(arr[j]):
			flag = True
			break
	if flag:
		fout.write( 'Case #%d: %d\n' % (i+1, sum))
	else:
		fout.write( 'Case #%d: %s\n' % (i+1, 'NO'))