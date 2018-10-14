def fsort(x,y):
	return x[0]-y[0]
def change(h,w,what,into,dr,H,W):
	if(dr[h][w]==what):
		dr[h][w]=into
	if(h>0 and dr[h-1][w]==what):
		change(h-1,w,what,into,dr,H,W)
	if(w>0 and dr[h][w-1]==what):
		change(h,w-1,what,into,dr,H,W)
	if(h<H-1 and dr[h+1][w]==what):
		change(h+1,w,what,into,dr,H,W)
	if(w<W-1 and dr[h][w+1]==what):
		change(h,w+1,what,into,dr,H,W)
f=open('in.txt','r')
T=int(f.readline())
for case in range(T):
	ts=f.readline().split()
	H=int(ts[0])
	W=int(ts[1])
	map=[]
	dr=[]
	for j in range(H):
		ta=[]
		tz=[]
		ts=f.readline().split()
		for n in ts:
			ta.append(int(n))
			tz.append('0')
		map.append(ta)
		dr.append(tz)
	sinklabels='abcdefghijklmnopqrstuvwxyz'
	freeLabel=0
	for h in range(H):
		for w in range(W):
			t=[]
			if(h>0 and map[h][w]>map[h-1][w]):
				t.append((map[h-1][w],h-1,w))
			if(w>0 and map[h][w]>map[h][w-1]):
				t.append((map[h][w-1],h,w-1))
			if(w<W-1 and map[h][w]>map[h][w+1]):
				t.append((map[h][w+1],h,w+1))
			if(h<H-1 and map[h][w]>map[h+1][w]):
				t.append((map[h+1][w],h+1,w))
			t.sort(fsort)
			if (len(t)>0):
				th=t[0][1]
				tw=t[0][2]
				if(dr[th][tw]=='0' and dr[h][w]=='0'):
					l=sinklabels[freeLabel]
					freeLabel=freeLabel+1
					dr[th][tw]=l
					dr[h][w]=l
				elif(dr[th][tw]=='0'):
					dr[th][tw]=dr[h][w]
				elif(dr[h][w]=='0'):
					dr[h][w]=dr[th][tw]
				else:
					setTo=min(dr[h][w],dr[th][tw])
					setFrom=max(dr[h][w],dr[th][tw])
#					print ":",setFrom,setTo,":"
					change(h,w,setFrom,setTo,dr,H,W)
			else:
				if(dr[h][w]=='0'):
					l=sinklabels[freeLabel]
					freeLabel=freeLabel+1
					dr[h][w]=l
	#normalize
	ac=0
	for h in range(H):
		if (ac>freeLabel-1):
			break
		for w in range(W):
			tac=sinklabels.find(dr[h][w])
			#print tac,dr[h][w],ac,sinklabels[ac]
			if(tac>ac+1):
				change(h,w,sinklabels[tac],sinklabels[ac+1],dr,H,W)
				ac=ac+1
			elif(tac>ac):
				ac=tac
			if (ac>freeLabel-1):
				break
#			for x in dr:
#				print x
#			print ";;;"
	print 'Case #'+str(case+1)+':'
	for h in dr:
		s=''
		for w in h:
			if (len(s)>0):
				s=s+' '
			s=s+w
		print s