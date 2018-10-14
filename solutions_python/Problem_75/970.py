def readlines():
	lines=[]
	file=open("input_large.in")
	
	while True:
		line=file.readline().rstrip()
		if not line:
			break
		lines.append(line)
		pass
	return lines

def reduce(word,combine,oppose):
	'''
	Until complete:
		For each letter, find a matching combination if possible
		If not possible, find shortest matching opposition
		If no oppositions, continue to the next letter
		Otherwise, erase/combine and start over
			from earliest changed letter
	'''
	index=0
	eltlist=''
	for l in word:
		eltlist=l+eltlist
		word=word[1:]
		key=eltlist[0:2]
		if key in combine:
			tword=combine[key]+eltlist[2:]
			eltlist=tword
		else:
			for elt in oppose:
				if elt[0]==l:
					i=eltlist[1:].find(elt[1])+1
					if i>0:
						eltlist=''
						#tword=eltlist[i+1:]
						#eltlist=tword
				elif elt[1]==l:
					i=eltlist[1:].find(elt[0])+1
					if i>0:
						eltlist=''
						#tword=eltlist[i+1:]
						#eltlist=tword


	#print eltlist[::-1]
	return eltlist[::-1]
def magicka(line):
	'''
	numcombine ... numoppose ... numletters string
	'''

	info=line.split(' ')
	numcombine=int(info[0])
	info.pop(0)
	combinations={}
	if numcombine > 0:
		for i in range(0,numcombine):
			key=info[i][0:2]
			combinations[key]=info[i][2]
			rkey=key[::-1]
			combinations[rkey]=info[i][2]
	info=info[numcombine:]
	numoppose=int(info[0])
	info.pop(0)
	oppose=[]
	if numoppose>0:
		for i in range(0,numoppose):
			oppose.append(info[i])
	info=info[numoppose:]

	word=info[1]

	ret=reduce(word,combinations,oppose)
	return ret


lines=readlines()
numlines=int(lines[0])
lines.pop(0)
f=open("out_large.out",'w')
for i in range(0,numlines):
	result=magicka(lines[i])
	s="["
	for l in result:
		s+="%s, " % l
	if len(s)>1:
		s=s[0:len(s)-2]
	s+="]"
	print >>f, "Case #%d: %s" % (i+1,s)
	
