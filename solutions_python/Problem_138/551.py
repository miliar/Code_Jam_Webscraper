def bigger(a,b):
	for i in range(len(a)):
		if b[i]>a[i]:
			return False
	return True
infile = open("D-large.in",'r')
T = int(infile.readline().rstrip())
for ix in range(T):
	print("Case #"+str(ix+1)+": ",end="")
	N = int(infile.readline().rstrip())
	a = sorted(infile.readline().rstrip().split(' '))
	b = sorted(infile.readline().rstrip().split(' '))
	wara = [float(x) for x in a]
	warb = [float(x) for x in b]
	war = 0
	for i in range(len(wara)):
		found = False
		for j in range(len(warb)):
			if warb[j]>wara[i]:
				warb.remove(warb[j])
				j-=1
				found = True
				break
		if not found:
			war+=1
	dwa = [float(x) for x in a]
	dwb = [float(x) for x in b]
	while(not bigger(dwa,dwb)):
		dwa = dwa[1:]
		dwb = dwb[:-1]
	print(len(dwa),war)

