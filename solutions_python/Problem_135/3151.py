#!/usr/bin/python

import sys
	
if 1==1:#sys.stdin.readline().rstrip("\n")=='Input':
	count = int(sys.stdin.readline(),10)
	for i in range(0,count):
		row1=int(sys.stdin.readline(),10)
		line1=sys.stdin.readline().rstrip("\n")
		line2=sys.stdin.readline().rstrip("\n")
		line3=sys.stdin.readline().rstrip("\n")
		line4=sys.stdin.readline().rstrip("\n")
		linef1=[]
		if row1==1:
			linef1=line1
		elif row1==2:
			linef1=line2
		elif row1==3:
			linef1=line3
		elif row1==4:
			linef1=line4
			

		row2=int(sys.stdin.readline(),10)
		line1=sys.stdin.readline().rstrip("\n")
		line2=sys.stdin.readline().rstrip("\n")
		line3=sys.stdin.readline().rstrip("\n")
		line4=sys.stdin.readline().rstrip("\n")
		linef2=[]
		if row2==1:
			linef2=line1
		elif row2==2:
			linef2=line2
		elif row2==3:
			linef2=line3
		elif row2==4:
			linef2=line4

		line1=linef1.split()
		line2=linef2.split()
		count=0
		res=0
		for a1 in line1:
			for a2 in line2:
				if a1==a2:
					count=count+1
					res=a1
		
		if count==0:
			print("Case #"+str(i+1)+": "+'Volunteer cheated!')

		elif count==1:
			print("Case #"+str(i+1)+": "+res)
		else:
			print("Case #"+str(i+1)+": "+'Bad magician!')

		

	
#End
