# -*- coding: utf-8 -*-

import sys

def testcase(case,smax,mem):
	
	inv = 0
	stand = 0
	case = case + 1
	

		
	if smax == 0:
		return(case,inv)
		
	else:
		if mem[0] != '0':
			stand = int(mem[0]) + stand
			
		for k in range(1,int(smax)+1):
			
			buf = k - stand

			if  mem[k] != '0' and buf > 0:
				inv = inv + buf
				stand = stand + buf + int(mem[k])
			elif  mem[k] != '0' and buf <= 0:
				stand = stand + int(mem[k])
			
			
		return (case,inv)




if __name__ == "__main__":
	
	case = 0
	
	fr = open('A-large.in','r')
	T = int(fr.readline())
	fw = open('A-large.out','w')
	
	for j in range(1,T+1):

		line = fr.readline()
		value = line.split()
		
		print value
		
		if len(value) != 2 or (len(value) == 2 and int(value[1]) == 0):
			j = j-1
			continue
			
		ans = testcase(case,value[0],value[1])
		case = ans[0]

		s = 'Case #'+str(ans[0])+': '+str(ans[1])
		fw.write(s+'\n')
		
	fr.close()
	fw.close()

	



