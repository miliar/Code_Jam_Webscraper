def plate(mush):
	x=firstcase(mush)		
	y=secondcase(mush)
	return x,y
def firstcase(mush):
	count=0
	for i in range(len(mush)-1):
		if((mush[i]-mush[i+1])>0):
			count+=mush[i]-mush[i+1]
	return count
def secondcase(mush):
	mini=0
	count=0
	for i in range(len(mush)-1):
		if((mush[i]-mush[i+1])>mini):
			mini=mush[i]-mush[i+1]
	for i in range(len(mush)-1):
		count+=min(mush[i],mini)
	return count
testcases=int(raw_input())
out=open("Output","w")
for i in range(testcases):
	n=int(raw_input())
	mush=map(int,raw_input().split(" "))
	y,z= plate(mush)
	out.write("Case #"+str(i+1)+": "+str(y)+" "+str(z)+"\n")
out.close()
