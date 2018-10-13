f = open('C-large.in', 'r')
g = open('Case1soln.dat', 'w')
g.close()
g = open('Case1soln.dat', 'a')
NumCases=int(f.readline())
for i in range (1,2*NumCases+1):
	line=f.readline().rstrip()
	words=line.split(' ')
	List=[]
	numlist=[]
	for k in range(1,25):
		List.append(0)

	if i%2==1:
		size=int(line)
	else:
		for j in range(0,size):
			num=int(words[j])
			k=21
			#print num
			while k>0:
				k=k-1
				#print List[k] 
				if num>=2**k:
					#print num,k,List[k]
					List[k]=List[k]+1;
					num=num-2**k
		OK=0
		for k in range(0,23):
			if List[k]%2==1:
				OK=1
		if OK==1:
			g.write('Case #' + str(i/2) + ': ' + 'NO\n')
			print 'Case #' + str(i/2) + ': ' + 'NO'
		else: 
			for j in range(0,size):
				numlist.append(int(words[j]))
			numlist.sort()
			numlist.pop(0)
			g.write('Case #' + str(i/2) + ': ' + str(sum(numlist)) + '\n')
			print 'Case #' + str(i/2) + ': ' + str(sum(numlist)) 
	
	
