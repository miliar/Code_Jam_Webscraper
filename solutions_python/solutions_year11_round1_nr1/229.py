def diag():
	pd = input()
	for i in range(1,100+1):
		if (float(pd)*i)/100 == int((float(pd)*i)/100):
			u = i
			break
	print u

def solveCase(N, pd, pg):
	if (pg == 100 and pd != 100) or (pg == 0 and pd!=0):
		return "Broken"
	for i in range(1,100+1):
		if (float(pd)*i)/100 == int((float(pd)*i)/100):
			u = i
			break
	if N >= u:
		return "Possible"
	else:
		return "Broken"

def main():
	T = input()

	for i in range(T):
		N, pd, pg = [int(j) for j in raw_input().split()]
		print "Case #%d: %s" % (i+1, solveCase(N,pd,pg))

main()
#diag()
