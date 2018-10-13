def solved(A, B):
	count = 0
	for loop in range(A, B+1):
		temp1 = str(loop)
		temp1 = temp1[-1]+temp1[:len(temp1)-1]
		if temp1[-1] == 0 or temp1[0] == 0:
			continue
		else:
			while int(temp1) != loop:
				if temp1[-1] == 0 or temp1[0] == 0:
					temp1 = temp1[-1]+temp1[:len(temp1)-1]
				else:
					if int(temp1) in range(A, B+1):
						count += 1
					temp1 = temp1[-1]+temp1[:len(temp1)-1]
				
			
#			temp1 = temp1[-1]+temp1[:len(temp1) - 2]
#			print temp1
#	print len(already)
	return count >> 1

if __name__ == '__main__':
	cases = int(raw_input())
	solution = []
	for i in range(cases):
		limit = raw_input().split(" ")
		A = int(limit[0])
		B = int(limit[1])
		solution.append(solved(A, B))
	for i in range(0,len(solution)):
		print 'Case #%d: %s'%(i+1, solution[i])
