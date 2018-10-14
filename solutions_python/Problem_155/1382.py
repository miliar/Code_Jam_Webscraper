def cumsum(arr):
	numArr = [int(each) for each in arr]
	l = [0]*len(numArr)
	l[0] = numArr[0]
	for i in range(1, len(arr)):
		l[i] = l[i-1] + numArr[i]
	return l	
	
def bruteforce(arr):
	ans = 0
	arr = [int(each) for each in arr]
	if arr[0] == 0:
		ans += 1
		arr[0] = 1
		
	for i in range(1, len(arr)):
		s = sum(arr[:i])
		if s < i:
			ans += i-s
			arr[i] = arr[i]+(i-s)
	return ans
	
def solve(arr):
	ans = 0
	if arr[0] == '0':
		ans += 1
		arr = '1' + arr[1:]
	l = cumsum(arr)
	for i in range(1, len(arr)):
		if l[i] < i+1: 
			if l[i-1] + int(arr[i]) >= i+1: 
				l[i] = l[i-1] + int(arr[i])
				continue
			#the previous guy was also lacking
			#then assume it to have been corrected to its mimimum.
			if l[i-1] < i:
				ans += 1
				l[i] = i+1
			else:
				ans += 1
				l[i] = i+1
		else:
			l[i] = l[i-1] + int(arr[i])
	return ans	

f = open("A-large.in", 'r')
f2 = open("output2.txt", 'w')	
t = int(f.readline())
for i in xrange(t):
	s = "Case #" + str(i+1) + ": "
	l = f.readline().split()[1]
	if i == t-1:
		f2.write(s+str(solve(l)))
	else:
		f2.write(s+str(solve(l))+'\n')
f.close()
f2.close()