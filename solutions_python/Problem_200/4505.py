nr_cases = int(input())

for i in range(nr_cases):
	nr = int(input())
	if nr >9:
		for n in range(0,nr):
			l=list(str(nr-n))
			if l == sorted(l): 
				print("Case #{}: {}".format(i+1,nr-n))
				break
	else:
		print("Case #{}: {}".format(i+1,nr))

