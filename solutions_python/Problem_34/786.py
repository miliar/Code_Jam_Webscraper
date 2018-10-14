li = raw_input().split()
L = int(li[0])
D = int(li[1])
N = int(li[2])

words = []
for i in xrange(D):
	words.append(raw_input())

for n in xrange(N):
	line = raw_input()
	start = 0
	#end = 1
	letters = []
	for i in xrange(L):
		if line[start] != '(':
			letters.append(line[start])
			start += 1
			#end += 1
		else:
			end = line.find(')', start)
			letters.append(line[start:end]);
			start = end + 1
	
	
	res = 0
	for word in words:
		b = True
		for i in xrange(L):
			if word[i] not in letters[i]: b = False
		
		if b: res += 1
	
	print 'Case #' + str(n+1) + ': ' + str(res)