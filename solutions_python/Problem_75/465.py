import string

f=open("magicka.txt","r")
s=f.readlines()
f.close()
length = str(s.pop(0))
retrn=""
for id in xrange(0,len(s)):
	swap={}
	delete=[]
	runes=[]
	ret=[]
	line=string.split(s[id].strip())
	index=1
	ind=0
	for ind in xrange(index,index+int(line[index-1])):
		swap[line[ind][:2]]=line[ind][2]
		swap[line[ind][1]+line[ind][0]]=line[ind][2]
	index=ind+1
	for ind in xrange(index+1,index+1+int(line[index])):
		delete.append((line[ind][0],line[ind][1]))
		delete.append((line[ind][1],line[ind][0]))
	if len(delete)==0:
		ind+=1
	runes=list(line[ind+2])
	#print swap,delete,runes
	reali=0
	for i in xrange(len(runes)):
		ret.append(runes[i])
		swapchar=""
		try:
			swapchar=swap["".join(ret[-2:])]
		except:
			pass #don't have to swap it
		if swapchar!="":
			ret=ret[:-2]+[swapchar]
			reali-=2
		hasToBreak=False
		for j in delete:
			if j[0]==ret[-1]:
				for k in ret:
					if k==j[1]:
						ret=[]
						reali=-1
						hasToBreak=True
						break
				if hasToBreak:
					break
		reali+=1
	print "Case #"+str(id+1)+": "+str(ret).replace("\'","")
	retrn+="Case #"+str(id+1)+": "+str(ret).replace("\'","")+"\n"
f=open("return.txt","w")
f.write(retrn)
f.close()
