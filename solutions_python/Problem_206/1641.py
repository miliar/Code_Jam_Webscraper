t = int(input())
case = 1
while(t):
	string = input()
	d, n = string.split()
	k = [0]*(int(n)+1)
	s = [0]*(int(n)+1)
	n = int(n)
	for i in range(1, n+1):
		temp = input()
		k[i],s[i] = temp.split()
		k[i] = int(k[i])
		s[i] = int(s[i])

	k[0] = 0
	s[0] = 10000
	time = [0]*(int(n)+1)
	for i in range(1, n+1):
		time[i] = float((int(d)-k[i])/s[i]) 
		
	for i in range(0, n-1):
		if(time[n-i] >= time[n-i-1]):
			time[n-i-1] = time[n-i]
			
		
			
	speed = int(d)/time[1]		
	

	
	print("Case #",case,": ",'%0.6f' % (speed), sep="")
	case = case + 1
	t=t-1