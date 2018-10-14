def solve(n):
	if len(n)==1:
		return int(n)
	flag = True
	for i in range(len(n)-1):
		if int(n[i]) > int(n[i+1]):
			if int(n[i:i+2]) ==10 and i ==0:
				n= n[0:i] + "9" + n[i+2:]
				for j in range(i+1,len(n)):
					n= n[0:j] + "9" + n[j+1:]
				#print n
			else :
				replace = str(int(n[i:i+2])-1) 
				if len(replace)==1:
					replace = "0" + replace
				n = n[0:i] + replace + n[i+2:]
				#print n
				for j in range(i+2,len(n)):
					n= n[0:j] + "9" + n[j+1:]
			#print n
			return solve(n)
	return int(n)


t = int(raw_input()) 
for i in xrange(1, t + 1):
  n = raw_input()
  solve(n)
  print "Case #{}: {}".format(i, solve(n))
  