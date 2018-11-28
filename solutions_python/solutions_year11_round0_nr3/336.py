inp = open("C-large.in")
outp = open("output-large.txt","w")

T=int(inp.readline())
i=0

while (i<T):
	N = inp.readline()
	line = inp.readline()
	cands = line.split(" ")
	
	
	outp.write("Case #"+str(i+1)+": ")
	
	susum = 0
	sum = 0
	min = int(cands[0])
	for j in range(len(cands)):
		susum^=int(cands[j])
		sum+=int(cands[j])
		if (int(cands[j])<min):
			min = int(cands[j])
		
	if (susum==0):
		outp.write(str(sum-min)+"\n")
	else:
		outp.write('NO\n')
		
	i+=1
