a=input()
for i in range(a):
	r=raw_input().split(" ")
	y=list(r[0])
	h=int(r[1])
	count=0
	for j in range(len(y)-h+1):
		if y[j]=="-":
			count+=1
			for u in range(h):
				if y[j+u]=="+":
					y[j+u]="-"
				else:
					y[j+u]="+"
	if "-" in y:
		print "Case #%d: %s"%(i+1,"IMPOSSIBLE")
	else:
		print "Case #%d: %d"%(i+1,count)
