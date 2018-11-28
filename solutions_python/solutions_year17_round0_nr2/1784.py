# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:59:29 2017

@author: adobe
"""
magic = lambda nums: int(''.join(str(i) for i in nums))
N=input()
ans=[]
for i in range(N):
	cur=raw_input()
	result=0
	digits=list(cur)
	nd=len(digits)
	digits=[int(a) for a in digits]
	digits.append(digits[-1])
	mini=int(min(digits))
	flag=-1
	for jj, contentt in enumerate(digits[:-1]):
		j=int(jj)
		content=int(contentt)
		if content<digits[jj+1]:
			result+=content*pow(10,nd-1-j)
		elif content==digits[jj+1]:
			result+=content*pow(10,nd-1-j)
			if flag==-1:
				flag=jj
		else:
			result+=content*pow(10,nd-1-j)-1
			break
	result_d=list(str(result))
	result_d=[int(b) for b in result_d]
	curans=magic(result_d)
	for jj,content in reversed(list(enumerate(result_d[:-1]))):
		# print jj
		if result_d[jj]>result_d[jj+1]:
			power=pow(10,nd-flag-1)
			curans=(curans/power)*power-1
	ans.append(curans)
# print ans

for j,con in enumerate(ans):
	print "Case #"+str(j+1)+": "+str(con) 