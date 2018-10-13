with open("B-large.in",'r') as f:
	case_num = 0
	out =""
	cases = int(f.readline())
	for i in xrange(cases):
		cakes_num = []
		D = int(f.readline())
		cakes = f.readline().split()
		for cake in cakes:
			cakes_num += [int(cake)]
		cake_max = max(cakes_num)
		cake_min = cake_max

		for j in xrange(1,cake_max+1):
			sum = j
			for k in xrange(D):
				if cakes_num[k] > j:
					if cakes_num[k] %j == 0:
						sum += (cakes_num[k]/j-1) 
					else:
						sum += (cakes_num[k]/j) 
			cake_min = min(cake_min,sum)
		case_num += 1

		out += "case #%d: %d \n" % (case_num,cake_min)

with open("B-large.out", 'aw') as f2:
    f2.write(out)





			
