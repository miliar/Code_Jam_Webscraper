p = raw_input()
for t in range(0,int(p)):
	r = []
	if(t>=1):
		l=raw_input()
	for i in range(0,4):
		l = raw_input()
		r.append(l)

	tot=0
	done =0
	for i in range(0,4):
		xcount=0
		ocount=0
		tcount=0
		for j in range(0,4):
			if r[i][j]=='X':
				xcount+=1
			if r[i][j]=='O':
				ocount+=1
			if r[i][j]=='T':
				tcount+=1
		if xcount+tcount==4:
			print "Case #"+str(t+1)+": "+"X won"
			done =1
		if ocount+tcount==4:
			print "Case #"+str(t+1)+": "+"O won"
			done = 1
		tot+=xcount+ocount+tcount
	
	if done==1:
		continue


	for i in range(0,4):
		xcount=0
		ocount=0
		tcount=0
		for j in range(0,4):
			if r[j][i]=='X':
				xcount+=1
			if r[j][i]=='O':
				ocount+=1
			if r[j][i]=='T':
				tcount+=1
		if xcount+tcount==4:
			print "Case #"+str(t+1)+": "+"X won"
			done=1
		if ocount+tcount==4:
			print "Case #"+str(t+1)+": "+"O own"
			done =1
	if done==1:
		continue


	xcount=0
	ocount=0
	tcount=0
	for i in range(0,4):
		if r[i][j]=='X':
			xcount+=1
		if r[i][i]=='O':
			ocount+=1
		if r[i][i]=='T':
			tcount+=1
	if xcount+tcount==4:
		print "Case #"+str(t+1)+": "+"X won"
		continue
	if ocount+tcount==4:
		print "Case #"+str(t+1)+": "+"O won"
		continue
	
	xcount=0
	ocount=0
	tcount=0
	for i in range(0,4):
		if r[i][3-i]=='X':
			xcount+=1
		if r[i][3-i]=='O':
			ocount+=1
		if r[i][3-i]=='T':
			tcount+=1
	if xcount+tcount==4:
		print "Case #"+str(t+1)+": "+"X won"
		continue
	if ocount+tcount==4:
		print "Case #"+str(t+1)+": "+"O won"
		continue
	if tot==16:
		print "Case #"+str(t+1)+": "+"Draw"	
	else:
		print "Case #"+str(t+1)+": "+"Game has not completed"
	