def sup(l):
	res=[l[0],0]
	act=[l[0],0]
	for i in l[1:]:
		res=[j^i for j in res]+[j for j in res]
		act=[j+i for j in act]+[j for j in act]
	return res,act

	
def decide(bag):
	tot=reduce(lambda x,y:x^y,bag)
	
	res,act=sup(bag)
	maxi=0

	acttot=sum(bag)
	for i in range(len(res)):
		if res[i]^tot==res[i] and act[i]!=acttot:
			maxi=max(maxi,act[i])
	
	return maxi


import sys
f=open(sys.argv[1],'r')
lines=f.readlines()

ncases=int(lines[0])
lines=lines[1:]
i=0
while i<ncases:
	line=lines[2*i+1]
	bag=[int(j) for j in line.split(' ')]
#	print 'bag: ', bag
	tot=decide(bag)

	if tot:
		print "Case #%d: %d"%(i+1,tot)
	else:
		print "Case #%d: %s"%(i+1,"NO")
	i+=1

