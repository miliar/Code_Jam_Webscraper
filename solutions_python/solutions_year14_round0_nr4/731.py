#!/usr/bin/env python

fo = open("D-large.in","r");
import sys
sys.stdout = open("D-large.out","w");
T = int(fo.readline())
for t in range(1, T + 1):
	count = 0
	count2 = 0
	n = int(fo.readline())
	vn = [0]*n
	kn = [0]*n
	nao = sorted(map(lambda x: float(x), fo.readline().split(' ')))
	ken = sorted(map(lambda x: float(x), fo.readline().split(' ')))
	if n == 1:
		#print nao[0],ken[0]
		if nao[0] < ken[0]:
			print 'Case #%d: 0 0' %(t)
		else:
			print 'Case #%d: 1 1' %(t)
	else:	
		for num in ken:
			for index in range(n):
	    			if nao[index] > num and vn[index] == 0:
					vn[index] =1
					#print 'nao value - %f  index - %d  ken value - %f ' %(nao[index],index,num)
					count+=1
					break
		
		# normal war
		nao.reverse()
		
		#kn = [0]*n
		
		top = n-1
		index=0
		for num in nao:
			#print 'nao value - %f  index - %d  top value - %f ' %(num,index,top)
			if ken[top] > num and kn[top] == 0:
				kn[top] =1;
				top-=1
				
			elif kn[index] == 0:
			#else:
				kn[index] = 1
				count2+=1
				index+=1
				
				
				
		print 'Case #%d: %d %d' %(t,count,count2)	
		


