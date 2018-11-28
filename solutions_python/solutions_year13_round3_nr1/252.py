ntest = int(raw_input())
for itc in xrange(ntest):
	print 'Case #%d:' % (itc+1),
	word, nString = raw_input().split()
	l = len(word)
	n = int(nString)
	total = 0
	vowels = ['a','e','i','o','u']
	for i in xrange(0,l-n+1):
		for j in xrange(i+n, l+1):
			subWord = word[i:j]
			subWordTrue = False
			for m in xrange(0, len(subWord)-n+1):
				three = 1
				for p in xrange(0,n):
					two = subWord[p+m] not in vowels
					three = three and two
					#print subWord, two, three, subWord[p+m]
				subWordTrue =  subWordTrue or three
			if (subWordTrue):
				total += 1
	print total