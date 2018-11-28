import string

f=open("candies.txt","r")
s=f.readlines()
f.close()

def splitCandies(id):
	line=string.split(s[id])
	xored=0
	minVal=int(line[0])
	minId=0
	for i in xrange(len(line)):
		xored=xored^int(line[i])
		if int(line[i])<minVal:
			minVal=int(line[i])
			minId=i
	if xored!=0:
		return "NO"
	else:
		line.pop(minId)
		sum=0
		for i in line:
			sum+=int(i)
		return sum
f=open("return.txt","w")
for id in xrange(2,len(s),2):
	r=splitCandies(id)
	print "Case #"+str(id/2)+": "+str(r)
	f.write("Case #"+str(id/2)+": "+str(r)+"\n")
f.close()
