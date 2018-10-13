timer=0
lines=[]
file = open('B-large.in','r')
allLines = file.readlines()
file.close()
for line in allLines:
	a = line.split()
	lines.append(a)

N=int(lines[0][0])

for count in range(N):
	seq=lines[count+1]
	com_no=int(seq[0])
	combs={};opp={}
	for i in range(com_no):
		string=seq[i+1]
		combs[string[0]+string[1]]=string[2]
	opp_no=int(seq[com_no+1])
	for i in range(opp_no):
		string=seq[com_no+i+2]
		if opp.has_key(string[1]):
			opp[string[1]].append(string[0])
		else:
			opp[string[1]]=[string[0]]
		if opp.has_key(string[0]):
			opp[string[0]].append(string[1])
		else:
			opp[string[0]]=[string[1]]
	i=opp_no+com_no+2
	n=int(seq[i])
	string=seq[i+1]
	final=[]
	for i in range(n):
		final.append(string[i])
		l=len(final)
		if l>=2:
			susp1=final[l-1]+final[l-2]
			susp2=final[l-2]+final[l-1]
			if combs.has_key(susp1)  or combs.has_key(susp2):
				final.pop();final.pop()
				try:	
					final.append(combs[susp1])
				except KeyError:
					final.append(combs[susp2])
			l=len(final)
			if opp.has_key(final[l-1]):
				for value in opp[final[l-1]]:
					if value in final:
						final=[]
	print 'Case #%d:' % (count+1),final
		#print 'l,bn,timer,O,B',l,bn,timer,o,b

