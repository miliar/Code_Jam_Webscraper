def flip(s,i,n):
	#print(s,i,n,"in")
	for k in range(i,i+n):
		if(s[k]=="-"):
			s=s[:k]+"+"+s[k+1:]
		else:
			s=s[:k]+"-"+s[k+1:]
	return s

fp1 = open("input.in",'r')
t = int(fp1.readline())
fp = open("output.txt",'w')

for turn in range(t):
	s,n = fp1.readline().split(" ")
	n = int(n)
	count=0
	for i in range(len(s)-n+1):
		#print(s,i,n)
		if(s[i]=="-"):
			s = flip(s,i,n)
			count+=1
	res = count
	if "-" in s:
		res = "IMPOSSIBLE"
	#print(res)
	if(turn==0):
		fp.write("Case #"+str(turn+1)+": "+str(res))
	else:
		fp.write("\nCase #"+str(turn+1)+": "+str(res))