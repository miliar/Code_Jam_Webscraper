import math

T = int(raw_input())
for t in range(T):
	D = input()
	inputi=raw_input().split()
	
	m1=0
	anterior=int(inputi[0])
	div=0
	for p in inputi:
		if anterior > int(p):
			m1+=anterior-int(p)
			if div < anterior-int(p):
				div=anterior-int(p)
		anterior=int(p)
	
	m2=0
	for p in range(len(inputi)-1):
		m2+=min(div,int(inputi[p]))
	
	print("Case #"+str(t+1)+": "+str(m1)+" "+str(m2))
