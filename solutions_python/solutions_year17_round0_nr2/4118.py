
t = int(input())
for i in range(t) :
	n = int (input())
	while n>0 :
		fg = 0 
		num = str(n)
		for j,d in enumerate(num) :
			if j == 0:
				continue
			if(num[j-1] > num[j]) :
				fg = 1;
				newNum = int(num[j:]) + 1
				n -= newNum
				break;
		if fg == 0 :
			print("Case #%d: %d" % (i+1,n))
			break
