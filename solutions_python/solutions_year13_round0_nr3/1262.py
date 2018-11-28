from math import sqrt

def pal(n):
	n = str(n)
	l = len(n)-1
	i = 0
	while i<=l:
		if(n[i]!=n[l]):
			return 0
		i = i+1
		l = l-1
	return 1

T = input()
for t in range(1,T+1):
	s = raw_input()
	l1,l2 = s.split()
	l1 = int(l1)
	l2 = int(l2)
	count = 0
	i = 0
	while i<=l2:
		k = i*i
		if(k>=l1 and k<=l2):
			if(pal(i)==1 and pal(k)==1):
				count = count+1
		elif(k>l2):
			break
		i = i+1
	print "Case #"+str(t)+": "+str(count)

	
