t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	n, m = input().split(" ")  # read a list of integers, 2 in this case
	m = int(m)
	s = 0
  
	while len(n) >= m:
  
		if n[0] == "-" :
			s = s+1
			
			for j in range(0, m):
				if n[j]=="+" :
					n = n[:j] + '-' + n[j+1:]
				else :
					n = n[:j] + '+' + n[j+1:]
		
		else : 
			n = n[1:]
		
	for j in range(0, len(n)) :
		if (n[j] == "-") :
			s = "IMPOSSIBLE"
	print("Case #{}: {}".format(i, s))
	