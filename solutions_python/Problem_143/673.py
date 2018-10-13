f = open('B-small-attempt0.in', 'r')
f1 = open('B-small.out', 'w')



#T=int(raw_input())
T=int(f.readline())

i=0
res=[]

i=0
while i < T:
	
	#s=raw_input().split()
	s=f.readline().split()
	#N=int(f.readline())
	A=int(s[0])
	B=int(s[1])
	K=int(s[2])
	
	count=0
	j=0
	while j < A:
		m=0
		while m < B:
			
			if m&j < K:
				count=count+1
			m=m+1
		j=j+1
	
	res.append(count)
	i=i+1

i=0
while i < T :
	f1.write("Case #"+str(i+1)+": "+str(res[i]))
	print "Case #"+str(i+1)+": "+str(res[i])
	if not i == (T-1):
		f1.write('\n')
	i=i+1

f.close()
f1.close()