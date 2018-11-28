fo = open("A-large.in","r")
content = fo.readlines();
T = int(content[0].strip())
for i in range(1,T+1):
	line = content[i]
	Smax = line.split(" ")
	row = Smax[1].strip()
	Smax = int(Smax[0].strip())
	if(Smax==0):
		print "Case #"+str(i)+": 0"
		continue;
	count = 0
	tf = 0
	k=0
	for p in row:
		frnd = 0
		if(k>count):
			frnd = (k-count)
			tf +=frnd
			count += frnd
		count += int(p)
		k+=1;
	print "Case #"+str(i)+": "+str(tf)
fo.close()