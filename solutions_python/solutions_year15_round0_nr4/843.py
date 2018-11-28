# -*- coding: utf-8 -*-

import sys

def testcase(case,x,r,c):
	
	case = case + 1
	
	
	if (r*c)%x != 0:
		return (case,'RICHARD')
		
	elif x==4 and (r*c== 8 or r*c== 4):
		return (case,'RICHARD')
		
	elif x==3 and (r*c== 3):
		return (case,'RICHARD')
		
	else:
		return (case,'GABRIEL')


if __name__ == "__main__":
	
	case = 0
	
	fr = open('D-small-attempt3.in','r')
	T = int(fr.readline())
	fw = open('D-small-attempt3.out','w')
	
	for j in range(1,T+1):

		line = fr.readline()
		value = line.split()
		
		print value
			
		ans = testcase(case, int(value[0]), int(value[1]), int(value[2]))
		case = ans[0]

		s = 'Case #'+str(ans[0])+': '+ans[1]
		fw.write(s+'\n')
		
	fr.close()
	fw.close()

	



