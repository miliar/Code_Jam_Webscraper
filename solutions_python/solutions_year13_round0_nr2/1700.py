f = open('/home/dexter/B-small-attempt0.in', 'r')

cases = int(f.readline())
def checkEqual3(lst):
    return lst[1:] == lst[:-1]

for i in range (0, cases):
	s=f.readline().split()
	lawn=[]
	for j in range(0,int(s[0])):
		l = f.readline().split()
		lawn.append(l)
	out = "YES"
	flag = False
	for k in xrange(0,int(s[0])):
		if not checkEqual3(lawn[k]):
			minimum=min(lawn[k])
			for t in range(0,len(lawn[k])):
				if lawn[k][t] == minimum:
					for j in  range(0,int(s[0])-1):
						if lawn[j][t] != lawn[j+1][t]:
							flag = True
							out = "NO"
							break
				if flag :
					break

		if flag:
			break

	print "Case #"+str(i+1)+": "+out

			

