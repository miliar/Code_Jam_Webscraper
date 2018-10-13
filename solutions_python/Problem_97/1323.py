

Ls = iter(map(lambda l:l.strip(),open("C-large.in").readlines()));

N = int(next(Ls));

for C in range(1,N+1):
	A,B=next(Ls).split()
	N=len(A);
	count=0;
	for i in range(int(A),int(B)):
		x = str(i);
		found=set([x]);
		for s in range(1,len(A)):
			y  = x[s:]+x[:s];
			if y>x and y<=B:
				found.add(x[s:]+x[:s]);
		count+=len(found)-1;
	print("Case #%d: %d"%(C,count));
