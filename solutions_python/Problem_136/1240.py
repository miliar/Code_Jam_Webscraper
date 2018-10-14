#Codejam QR
#Problem B. Cookie Clicker Alpha
#Submitted By : Yogendra Tank

cases = input()
for case in range(cases):
	(c,f,x) = map(float,raw_input().split())
	#initial state
	
	rate=2
	ansF = 0.0
	ansD = 0.0
	ans=0
	#Start Counter
	while (1):
		#Counting Time for farm and direct
		tD = (x/rate)
		tF = ((c/rate)+(x/(rate+f)))
		if (tD > tF):
			#Adding Farm Change
			ans +=(c/rate)
			rate += f
		else:
			ans +=tD
			break
	print 'Case #'+str(case+1)+': '+str(ans)