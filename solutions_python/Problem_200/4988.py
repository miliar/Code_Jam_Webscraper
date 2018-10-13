t = int(raw_input())  # read a line with a single integer
for i in range(1, t + 1):
	a = int(raw_input())
	while True : 
		li = [int(j) for j in str(a)]
		
		if sorted(li) == li:
			print "Case #{}: {}".format(i, a)
			break
		a-=1

  
  
