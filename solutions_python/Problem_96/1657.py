def solved(arr):
	count = 0
	dancers = arr[0] = int(arr[0])
	surprise = arr[1] = int(arr[1])
	base = arr[2] = int(arr[2])
	for i in range(3, len(arr)):
		arr[i] = int(arr[i]) - base
		#print arr[i]
		if surprise != 0 and arr[i] >= 0:
			if arr[i] >= 2*base:
				#print 'chutiyapa'
				count += 1
			elif(base - (arr[i] / 2 ) <= 1):
				#print 'wtf'
				count += 1
			elif(base - (arr[i] / 2 ) > 1) and (base - (arr[i] / 2 ) <= 2):
				surprise -= 1
				count += 1
				#print 'fuck'
		elif surprise == 0 and arr[i] >= 0:
			if(base - (arr[i] / 2) <= 1) or (arr[i] >= 2*base):
	#			print 'yaha'
				count += 1
		
	#print arr, count
	return count
	



if __name__ == '__main__':
	solution = []
	cases = int(raw_input())
	for i in range(cases):
		test = raw_input().split(" ")
		solution.append(solved(test))
	for i in range(len(solution)):
		print 'Case #%d: %d'%(i+1, solution[i])
