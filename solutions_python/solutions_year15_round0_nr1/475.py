with open('in.txt','rb') as fin, open('output.txt','w') as fout:
	count=0
	case = 1
	for line in fin:
		count += 1
		if count==1:
			continue

		m, a = line.split();
		shy=0
		res=0
		cur=0
		for c in list(a):
			if int(c)>0 and cur+res < shy:
				res += shy-cur-res
			cur += int(c)
			shy += 1
		fout.write("Case #" + str(case) + ": " + str(res) + "\n")
		case += 1