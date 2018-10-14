def no(x):
	if (x%3==0): return x/3
	if (x%3==1): return (x-1)/3+1
	if (x%3==2): return (x-2)/3+1
def st(x):
	if (x%3==0 and x/3 >= 1 and x/3 <= 10): return x/3+1
	elif (x%3==1 and (x+2)/3 >= 2 and (x+2)/3 <= 10): return (x+2)/3
	elif (x%3==2 and (x+4)/3 >= 2 and (x+4)/3 <= 10): return (x+4)/3

fin = open("input.txt", "r")
fout = open("output.txt", "w")

ll = fin.readlines()

i=1
for l in ll[1:]:
	N,S,P = map(int,l.split()[:3])
	arr = map(int,l.split()[3:])
	cnt = 0

	for v in arr:
		normal = no(v)
		star = st(v)

		if (normal >= P): cnt += 1
		elif (S > 0 and star >= P):
			cnt += 1
			S -= 1
	fout.write( "Case #%d: %d\n" % (i,cnt) )

	i+=1
