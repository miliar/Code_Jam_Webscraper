import sys
T = int(sys.stdin.readline())
for i in range(T):
	arr = [int(x) for x in sys.stdin.readline().split(' ')]
	
	N,S,p = arr[0:3]
	goos = arr[3:]
	res = 0
	
	for g in goos:
		mod = g%3
		if mod == 0:
			if int(g/3) >= p:
				res += 1
			else:
				if S > 0 and int(g/3) +1 >= p and int(g/3) +1 <= g:
					res +=1
					S -=1
		elif mod == 1:
			if int(g/3) +1 >= p and int(g/3) +1 <= g:
				res += 1
		else:
			if int(g/3) +1 >= p and int(g/3) +1 <= g:
				res += 1
			else:
				if S > 0 and int(g/3) +2 >= p and int(g/3) +2 <= g:
					
					res +=1
					S -=1
					

	print( "Case #"+str(i+1)+": "+str(res))


	