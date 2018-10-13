import sys

inputlist=sys.stdin.read().splitlines()

cases=inputlist[0]
i=1
count=1
output=[]
while i<len(inputlist):
	SEdict={}
	engineQueue=[]
	queries=[]
	switch=0
	numSE=int(inputlist[i])
	#remember to increment i
	for j in range(1,numSE+1):
		SEdict[inputlist[i+j]]=0
		engineQueue.append(inputlist[i+j])
	i+=numSE+1
	numQ=int(inputlist[i])
	for j in range(1,numQ+1):
		queries.append(inputlist[i+j])
	for each in queries:
		if SEdict.has_key(each)and SEdict[each]!=1:
			del engineQueue[engineQueue.index(each)]
			SEdict[each]=1
		if len(engineQueue)==0:
			for engines in SEdict.keys():
				engineQueue.append(engines)
				SEdict[engines]=0
			SEdict[each]=1
			del engineQueue[engineQueue.index(each)]
			switch+=1
	output.append('Case #'+str(count)+': '+str(switch))
	i+=numQ+1
	count+=1

for each in output:
	print each
	


