def run(dic,words):
	count = 0
	for word in dic:
		count += 1
		for i in xrange(len(word)):
			if not word[i] in words[i]:
				count -= 1
				break

	return count		


'''	if n>=len(words):
		#print w
		if dic.has_key(w):
			return 1
		else:
			return 0
	total = 0
	for i in xrange(len(words[n])):
		total += run(dic,words, w + words[n][i],n+1)
	return total'''

(l,d,n) = raw_input().split()
dic = [] 
for i in xrange(int(d)):
	dic.append(raw_input())
for i in xrange(int(n)):
	words = []
	mode = 0
	for el in raw_input():
		if mode == 0 and el == '(':
			mode = 1
			wtmp = ""
		elif mode == 0:
			words.append(el)
		elif mode == 1 and el == ')':
			mode = 0
			words.append(wtmp)
		else:
			wtmp += el

	print "Case #"+str(i+1)+":",run(dic,words)

