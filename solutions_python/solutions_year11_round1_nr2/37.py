f = open("b.in")
d = f.read()
f.close()

d = d.split("\n")

t = int(d[0])

f = open("b.out", "w")
ti = 1
for i in xrange(t):
	n, m = d[ti].split(" ")
	n = int(n)
	m = int(m)
	ti += 1
	
	D = []
	for j in xrange(n):
		D += [d[ti]]
		ti += 1
	
	L = []
	for j in xrange(m):
		L += [d[ti]]
		ti += 1
	
	SOL = []
	for l in L:
		_points = 0
		W = D[0]
		for w in D:
			#print "-->", w
			points = 0
			
			words = []
			for w2 in D:
				if len(w2) == len(w):
					words += [w2]
			#print words
				
			for c in l:
				#print words
				#raw_input("s")
				#print c, c in "".join(words)
				if c in "".join(words):
					words2 = []
					for w2 in words:
						flag = True
						for j in xrange(len(w)):
			#				print "       ", (c == w[j]), (c == w2[j]), w2
							if (c == w[j]) != (c == w2[j]):
								flag = False
						if flag:
							words2 += [w2]
					words = words2
					#print words
					if not c in w:
						points += 1
					if words == [w]:
						break
			#print "Con", w, "haria", points, "puntos"
			if points > _points:
				W = w
				_points = points
		#print "----SOL:", W
		SOL += [W]
	
	S = "Case #%d: %s" % ((i+1), " ".join(SOL))
	print S
	f.write("%s\n" % S)
f.close()





















exit()

f = open("b.in")
d = f.read()
f.close()

d = d.split("\n")

t = int(d[0])


f = open("b.out", "w")
ti = 1
for i in xrange(t):
	n, m = d[ti].split(" ")
	n = int(n)
	m = int(m)
	ti += 1
	
	D = []
	for j in xrange(n):
		k = 0
		for c in "abcdefghijklmnopqrstuvwxyz":
			if c in d[ti]:
				k += 1
		D += [[d[ti], k, True, len(D)]]
		ti += 1
	
	wordsWithLetter = dict()
	for c in "abcdefghijklmnopqrstuvwxyz":
		wordsWithLetter[c] = []
	
	for j in xrange(len(D)):
		for c in D[j][0]:
			wordsWithLetter[c] += [D[j]]
	
	SOL = []
	L = []
	for j in xrange(m):
		L += [d[ti]]
		perd = 0
		curr = d[ti]
		print curr
		for ci in xrange(len(curr)-1, -1, -1):
			for word in wordsWithLetter[curr[ci]]:
				if D[word[3]][2]:# and ci - word[1] > perd:
					perd = ci - word[1]
					WW = word[0]
					D[word[3]][2] = False
					print WW, perd, ci, word[1]
		print WW
		
		"""
		nums = []
		guessed = [False] * len(D)
		count = []
		_count = []
		for e in D:
			nums += [[False] * 26]
			count += [0]
			_count += [0]
			for c in e:
				if not nums[-1][ord(c) - ord('a')]:
					count[-1] += 1
					_count[-1] += 1
				nums[-1][ord(c) - ord('a')] = True
		
		word = ""
		curr = d[ti]
		PERDIDOS = 0
		for II in xrange(len(curr)):
			c = curr[II]
			for j in xrange(len(D)):
				if nums[j][ord(c)-ord('a')]:
					nums[j][ord(c)-ord('a')] = False
					count[j] -= 1
					if count[j] == 0 and (II-_count[j] > PERDIDOS):
						word = D[j]
						PERDIDOS = II - _count[j]
		print word
		"""
		ti += 1
	
	print SOL
	S = "Case #%d: %s" % ((i+1), "asd")
	print S
	f.write("%s\n" % S)
f.close()

