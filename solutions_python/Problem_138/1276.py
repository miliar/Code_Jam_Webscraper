# -*- coding:utf-8 -*-

fr = open("D-large.in","r")
fw = open("D-large.out","w")
lines  = int(fr.readline())
i = 1

while i<=lines:
	#Problem Start	
	N = int(fr.readline())
	
	CN1=[]
	CK1=[]
	CN2=[]
	CK2=[]
	
	l = fr.readline()
	s = l.split()
	for j in range(0,N):
		CN1.append(float(s[j]))
		CN2.append(float(s[j]))
	l = fr.readline()
	s = l.split()
	for j in range(0,N):
		CK1.append(float(s[j]))
		CK2.append(float(s[j]))
	
	CN1.sort()
	CK1.sort()
	CN2.sort()
	CK2.sort()
	
	#print(i,CN1)
	#print(i,CK2)
	
	# Deceitful War
	DWP=0
	while 0<len(CN1):
		if CN1[0]<CK1[0]:
			CN1.pop(0)
			CK1.pop()
		else:
			CN1.pop(0)
			CK1.pop(0)
			DWP=DWP+1
			
	# War
	WP=0
	CN2.reverse()
	CK2.reverse()
	while 0<len(CN2):
		if CN2[0]>CK2[0]:
			CN2.pop(0)
			CK2.pop()
			WP=WP+1
		else:
			CN2.pop(0)
			CK2.pop(0) 
	
	fw.write("Case #{}: {} {}\n".format(i,DWP,WP))
	
	#End
	i=i+1



fr.close
fw.close