f=open("input")
output=open("output_1","w+")
no_of_test_cases = int(f.readline())
test_cases = f.readlines()
case_count = 0
for case in test_cases:
	case_count+=1
	case = case.strip().split(" ")
	n = int(case.pop(0))
	total_s = int(case.pop(0))
	p = int(case.pop(0))
	count = 0
	used_s = 0
	scores = case[:]
	if p is 0:
		count=n
	else:
		pos = []
		for t in range(0, n):
			score = scores[t]

			for x in range(p,11):
				a = 3*x 
				b = a -1  
				c = a -2 
				d = a -3 
				e = a -4
				
				if (int(score) == a or int(score) == b or int(score) == c) and (int(score) is not 0):
					count+=1
					pos.append(t)
					break
		for t in range(0, n):
			if t not in pos:
				score = scores[t]
				for x in range(p,11):
					a = 3*x 
					b = a -1  
					c = a -2 
					d = a -3 
					e = a -4					
					if (int(score) == d or int(score) == e) and (used_s < total_s) and (int(score) is not 0):
						count+=1
						used_s+=1
						break
	if n < count:
		print "Error", n, count
	q = "Case #"+str(case_count)+": "+str(count)+chr(10)
	output.write(q)
output.close()

