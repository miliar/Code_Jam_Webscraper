def firstInversion(n):
	global l
	inv = -1
	for i in range(1,n):
		if l[i-1]>l[i]:
			inv=i
			break
	return inv

for t in range(int(input())):
	s = input()
	n = len(s)
	while n:
		l = [int(i) for i in s]
		inv = firstInversion(n)
		if inv==-1: break
		else:
			nx = int(s[0:inv])-1
			if not nx: nx=""
			s = str(nx)+"9"*(len(s)-inv)
			n = inv
	print("Case #{0}: {1}".format(t+1,s))
