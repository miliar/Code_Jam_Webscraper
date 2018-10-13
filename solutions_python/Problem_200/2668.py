import math
f= open("data")
T = int(f.readline().strip("\n"))
case = 0
while T > 0:
	case += 1
	T -= 1
	line = f.readline().strip("\n")
	num = line
	ans = ''
	for i in range(len(num)):
		base = num[i]*(len(num)-i)
		base = int(base)
		#print 'base',base,num[i:]
		if int(base) > int(num[i:]):
			ans += str(int(num[i])-1)+'9'*(len(num)-i-1)
			break
		ans += num[i]
	print "Case #"+str(case)+":",int(ans)
