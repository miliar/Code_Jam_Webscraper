#! /usr/bin/python

case=1
f = open("inpfile","r")
f.readline()
for line in f.readlines():
	a=[]
	line1=line.strip("\n")
	for z in line1:
		a.append(z)
	b=[]
	for x in a:
		if x not in b: 
			b.append(x)

	radix = len(b)
	if radix==1 : 
		d={b[0]:1}
		radix=2
	else :
		count=0
		d={b[0]:1,b[1]:0}

		count = 2
		for i in b[2:]:
			d[i] = count
			count=count+1

	out=""
	for j in a:
		out=out+str(d[j])

	total=0
	alen = len(a)
	for i in out:
		alen = alen-1
		total = total + (int(i)*(radix ** alen))
	
	print "Case #" + str(case) + ": " + str(total)
	case = case+1
