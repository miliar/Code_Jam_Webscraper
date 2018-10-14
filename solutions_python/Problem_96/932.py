import sys

f = open(sys.argv[1],"r")
n = int(f.readline())

for c in range(n):
	i = map(int,f.readline().split())
	N = i[0]
	s = i[1]
	p = i[2]
	i = sorted(i[3:], reverse=True)
	count = 0
	if p==0:
		print "Case #" + str(c+1) + ": " + str(N)
	else:
		for j in i:
			if j>= 3*p-2:
				count+=1
			elif j>max(3*p-5,0):
				if s==0:
					break
				s-=1
				count+=1
		print "Case #" + str(c+1) + ": " + str(count)
	#notSurp = [j for j in i if j>=(3*p-2)]
	#print "Case #" + str(c+1) + ": " + str(len(notSurp)+min(len([j for j in i if j>=p and j not in notSurp]),s)) + " " +",".join(map(str,i))

	#print s, p, i[3:]
	
