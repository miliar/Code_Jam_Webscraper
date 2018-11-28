
f=open('A-small-attempt2.in','r');
s=open('result.txt','w');
i=1;
n = int(f.readline())

if n>=1 and n<=100:
	while i<=n:
		val1 = int(f.readline())
		if val1 <1 or val1 > 4:
			break
		k=1
		while k<=4:
			if k == val1:
				ligne1 = (f.readline().rstrip('\n\r')).split(" ");
			else:
				f.readline();
			k+=1;
		k=1;
		val2 = int(f.readline());
		if val2 <1 or val2>4:
			break
		while k<=4:
			if k == val2:
				ligne2 = (f.readline().rstrip('\n\r')).split(" ");
			else:
				f.readline();
			k+=1;

		cpt=0;
		elt = 0;
		for val in ligne1:
			if val in ligne2:
				cpt,elt= cpt+1,int(val);
		if cpt == 0:
			var="Case #"+str(i)+": Volunteer cheated!\n"
		elif cpt == 1:
			var="Case #"+str(i)+": "+str(elt)+"\n"
		elif cpt:
			var="Case #"+str(i)+": Bad magician!\n"
		s.write(var)
		i+=1
