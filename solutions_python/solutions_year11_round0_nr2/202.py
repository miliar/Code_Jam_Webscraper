import sys
def f(ii,first):
	s=first.split()
	
	combn=int(s[0])
	comb=s[1:combn+1]
	oppn=int(s[combn+1])
	opp=s[combn+2:combn+oppn+2]
	stringa=s[len(s)-1]

	#print s, comb, opp,stringa

	a=""
	for i in stringa:
		a+=i
		for k in comb:
			while a[-2:]==k[0:2] or a[-2:]==k[1:2]+k[0:1]:
				a=a[0:-2]+k[2]

		
		for k in opp:
			p=0
			r=0
			for m in a:
				if m==k[0]:
					p=1
				if m==k[1]:
					r=1
			if p+r==2:
				a=""

		#print a
		ff=str(list(a)).replace("'","")
		#print ff
		
		

	print "Case #"+str(ii)+": " + ff

b = open(sys.argv[1]).readlines()

for i in range(int(b[0])):
	f(i+1,b[i+1])


