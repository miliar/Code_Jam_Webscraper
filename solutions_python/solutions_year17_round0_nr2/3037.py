T = int(input())

for i in range(1, T+1):
	N = input()
	Num = int(N)
	N = list(N)
	s = N
	tidy = ""
	tid = N[0]*len(N)

	while(tid <= ("".join(s)) ):
		tidy += s[0]
		s = s[1:]
		if(len(s)==0):
			break
		tid = s[0]*len(s)

	if(len(s)!=0):
		z = str(10**(len(tid)-1)*int(tid[0])-1)
	else:
		z = ""

	print("Case #"+str(i)+": " + tidy+z )
