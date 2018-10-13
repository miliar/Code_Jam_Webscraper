f = open('large.in', 'r')
r = open('res.txt','w+')

n = int(f.readline())
res = ""

for i in range(0,n):
	print i
	l1 = f.readline()
	l1 = l1[:-1]
	l2 = f.readline()
	l2 = l2[:-1]
	l3 = f.readline()
	l3 = l3[:-1]
	l4 = f.readline()
	l4 = l4[:-1]
	f.readline()

	c1 = l1[0]+l2[0]+l3[0]+l4[0]
	c2 = l1[1]+l2[1]+l3[1]+l4[1]
	c3 = l1[2]+l2[2]+l3[2]+l4[2]
	c4 = l1[3]+l2[3]+l3[3]+l4[3]
	
	d1 = l1[0]+l2[1]+l3[2]+l4[3]
	d2 = l1[3]+l2[2]+l3[1]+l4[0]
	
	full = True
	xwin = False
	owin = False
	
	if ("." in l1+l2+l3+l4):
		full = False
	tset = [l1,l2,l3,l4,c1,c2,c3,c4,d1,d2]
	if ("XXXX" in tset) or ("XXXT" in tset) or ("XXTX" in tset) or ("XTXX" in tset) or ("TXXX" in tset):
		xwin = True
	if ("OOOO" in tset) or ("OOOT" in tset) or ("OOTO" in tset) or ("OTOO" in tset) or ("TOOO" in tset):
		owin = True
	
	res +="Case #"+str(i+1)+": "
	
	if (xwin and owin):
		print "ERREUR"
	elif (xwin):
		res += "X won\n"
	elif (owin):
		res += "O won\n" 
	elif (full):
		res += "Draw\n"
	else:
		res += "Game has not completed\n"
		
r.write(res)
r.close()