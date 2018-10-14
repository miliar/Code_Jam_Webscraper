f = open('B-large.in', 'r')
f1 = open('cc_large.out', 'w')

#T=int(raw_input())
T=int(f.readline())

i=0
res=[]

i=0
while i < T:
	#s=raw_input().split()
	s=f.readline().split()
	C=float(s[0])
	F=float(s[1])
	X=float(s[2])
	
	#Initializing Defaults
	TT=0.0
	P=2
	
	while (1.0*X/P) > ( 1.0*C/P + 1.0*X/(P+F)) :
		TT=TT+1.0*C/P
		#print 1.0*C/P
		P=P+F
	
	TT=TT+1.0*X/P
	res.append(str(TT))
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