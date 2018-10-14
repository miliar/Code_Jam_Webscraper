with open("A-large.in",'r') as f:
	case_num =0
	cases = f.readline()
	out =""
	for line in f:
		sum = 0
		num = 0
		case_num = case_num+1
		case = line.split()
		s_max = case[0]
		s_n = 0
		for s in case[1]:
			if int(s) > 0:
				kk = s_n-sum
				if  kk > 0:
					num = num + kk
					sum = s_n + int(s)
				else:
					sum = sum + int(s)
			s_n = s_n + 1
			
		out += "case #%d: %d \n" % (case_num,num)

with open("A-large.out", 'aw') as f2:
    f2.write(out)



