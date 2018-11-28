class stall:
	def __init__(self,left,right,num):
		self.num = num
		self.right = right
		self.left = left
		self.isoccupied=0
		


t = int(raw_input())  # read a line with a single integer
for p in xrange(1, t + 1):
	N, k = [int(s) for s in raw_input().split(" ")]
	stallsList = []
	for x in xrange(0,N):
		stallsList.append(stall(-1,N,x))
	maxtempvalue = N-1
	mintempvalue = 0
	if N%2 == 0:
		mintempvalue = 1
	for x in xrange(0,k):
		mintemp = []
		maxtemp = []
		mintempindex = []
		for i in xrange(0,N):
			if stallsList[i].isoccupied==0:
				mintempindex.append(i)
				mintemp.append(min((stallsList[i].num-stallsList[i].left-1),(stallsList[i].right-stallsList[i].num-1)))

		indexarray = []
		mintempvalue = max(mintemp)
		count = 0
		for i in xrange(0,len(mintemp)):
		 	if mintempvalue==mintemp[i]:
		 		indexarray.append(mintempindex[i])
		 		index = mintempindex[i]
		 		count+=1
		if(count>1):
			count1=0
			for ind in indexarray:
				maxtemp.append(max((stallsList[ind].num-stallsList[ind].left-1),(stallsList[ind].right-stallsList[ind].num-1)))
			maxtempvalue = max(maxtemp)
			for i in xrange(0,len(maxtemp)):
				if maxtempvalue==maxtemp[i]:
			 		index = indexarray[i]
					count1+=1
			if count1>1:
		 		for i in xrange(0,len(maxtemp)):
		 			if maxtempvalue==maxtemp[i]:
		 				finalindex = indexarray[i]
		 				break
			else:
		 		finalindex = index
		else:
			finalindex = index
		stallsList[finalindex].isoccupied = 1
		for i in xrange(0,N):
			if i==finalindex:
				continue
			elif i<finalindex:
				if stallsList[i].right>finalindex:
					stallsList[i].right=finalindex
			else:
				if stallsList[i].left<finalindex:
					stallsList[i].left=finalindex
		mintempvalue = min((stallsList[finalindex].num-stallsList[finalindex].left-1),(stallsList[finalindex].right-stallsList[finalindex].num-1))
		maxtempvalue = max((stallsList[finalindex].num-stallsList[finalindex].left-1),(stallsList[finalindex].right-stallsList[finalindex].num-1))

	print "Case #{}: {} {}".format(p, maxtempvalue, mintempvalue)
