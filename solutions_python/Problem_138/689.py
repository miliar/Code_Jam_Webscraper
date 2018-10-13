f = open('D-large.in', 'r')
f1 = open('dwar_large.out', 'w')

#T=int(raw_input())
T=int(f.readline())

i=0
res=[]


while i < T:
	#N=int(raw_input())
	N=int(f.readline())
	
	#s=raw_input().split()
	s=f.readline().split()
	s1=[float(x) for x in s]
	s1=sorted(s1)
	
	#s=raw_input().split()
	s=f.readline().split()
	s2=[float(x) for x in s]
	s2=sorted(s2)
	
	#For playinf Deceitful War
	j=0
	k=0
	count1=0
	while j < N:
		if s1[j] > s2[k]:
			k=k+1
			count1=count1+1
			#print s1[j], count1
		j=j+1
	#for playing war
 	count=0
	j=0
	k=0
	while j < N:
		if s2[j]>s1[k]:
			count=count+1
			k=k+1
		j=j+1
	
	res.append(str(count1)+' '+str(N-count))
	i=i+1

i=0
while i < T :
	f1.write("Case #"+str(i+1)+": "+res[i])
	#print "Case #"+str(i+1)+": "+res[i]
	if not i == (T-1):
		f1.write('\n')
	i=i+1
f.close()
f1.close()