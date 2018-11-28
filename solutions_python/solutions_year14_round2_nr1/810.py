#fName = "test"
fName = "A-small-attempt0"
#fName = "A-large"

fin = open(fName + ".in", 'r')
fout = open(fName + ".out", 'w')

def simps(s):
	x = ""
	res = ""
	num = list()
	count =-1
	for i in range(len(s)):
		if s[i]!=x:
			res += s[i]
			x = s[i]
			num.append(1)
			count +=1
		else :
			num[count] += 1		
	return res,num

#print simps("aabbccccde")

T = int(fin.readline())

for t in range(T):	
	N = int(fin.readline())
	l = fin.readline().strip()
	refs, nums = simps(l)
	L = len(refs)
	num = [[0 for i in range(N)] for n in range(L)]
	#print num
	#print num[N-1][0]
	out = 0
	for n in range(N):
		if n!=0:
			l = fin.readline().strip()
		s,q = simps(l)
		if s!=refs:
			out = -1
			break
		else:
			for j in range(L):
				num[j][n] = q[j]
	#print num	
	#print out
	if out != -1:
		for i in range(L):
			op = [x for x in num[i]]
			op.sort()
			nbop = [abs(a-b) for a,b in zip(op[:N-1:],op[1::])]
			out += sum(nbop)
	
	if out == -1:
		fout.write("Case #" + str(t+1) + ": " + "Fegla Won" +"\n")
	else :
		fout.write("Case #" + str(t+1) + ": " + str(out) +"\n")
fin.close()
fout.close()
