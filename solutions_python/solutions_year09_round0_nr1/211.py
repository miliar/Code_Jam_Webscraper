import sys, os

filename = "A-large"

path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".in"))
reader = open(path, "rb")
path = os.path.normpath(os.path.join(os.path.dirname(__file__), filename+".out"))
writer = open(path,"w")
nums = reader.readline().rstrip().split(' ')
(L,D,N) = [int(x) for x in nums]

pd = []
i=0
while i<D:
	i+=1
	tword = reader.readline().rstrip()
	pd.append(tuple([1<<(ord(x)-ord('a')) for x in tword]))

	
caseno = 1
case = reader.readline()
while case != '':
	pat = case.rstrip()
	curval = 0
	inpar = False
	ppat = []
	for c in pat:
		if c=='(':
			inpar = True
			curval = 0
			continue
		elif c==")":
			inpar = False
			ppat.append(curval)
			curval = 0
			continue
		if inpar:
			curval = curval | (1<<(ord(c)-ord('a')))
		else:
			curval = curval | (1<<(ord(c)-ord('a')))
			ppat.append(curval)
			curval = 0
	count = 0
	for word in pd:
		match = True
		j = 0
		while j < len(word):
			if (word[j] & ppat[j])==0:
				match = False
				break
			j+=1
		if match:
			count+=1
	writer.write("Case #%s: %s\n" % (str(caseno),count))
	caseno+=1
	case = reader.readline()

writer.close()