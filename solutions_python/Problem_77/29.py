T=int(raw_input())
for t in range(T):
	raw_input()
	line=raw_input().split()
	d=[]
	n=[]
	for i in range(len(line)):
		d.append(int(line[i]))
		n.append(int(line[i]))
	n.sort()
	count=0
	for i in range(len(d)):
		if d[i]!=n[i]: count+=1
	print "Case #%d: %.6f" %(t+1,count)