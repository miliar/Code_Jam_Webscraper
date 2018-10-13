#FairAndSquare
import math

def rev(str):
	ret = str[-1]
	for i in range(2, len(str) + 1, 1):
		ret += str[-i]
	return ret

t = int(raw_input())

for j in range(0, t, 1):
	line = raw_input().split()
	A = int(line[0])
	B = int(line[1])
	
	count = 0

	curNum = int(math.sqrt(A))

	newNum = curNum * curNum
	
	if(newNum != A):
		curNum += 1
		A = newNum
		A += curNum
		A += curNum - 1
	else:
		if str(A) == rev(str(A)) and str(curNum) == rev(str(curNum)):
			#print A, "---", curNum
			count += 1
			curNum += 1
			A += curNum + curNum -1
			


		
	while(A <= B):
		s_num = str(A)
	
		if(str(A) == rev(str(A)) and str(curNum) == rev(str(curNum))):
			count += 1
			#print A, "---", curNum
		
		A += curNum
		curNum += 1
		A += curNum
	
	
	print "Case #"+str(j+1)+": "+str(count)
	





