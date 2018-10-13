#task2

f = open('B-large.in','r')
ans = open('ans.txt', 'w')

T = int(f.readline())

for k in range(T):
	line = f.readline()
	nums = line.split(' ')
	N = int(nums[0])
	S = int(nums[1])
	p = int(nums[2])
	arr = [int(num) for num in nums[3:]]
	#print(N,S,p,arr)

	res = 0

	for i in arr:
		left = i - p
		if left<0:
			continue
		#print ('left: ',left)
		n1 = left//2
		n2 = left - n1
		if n1 < 0 or n2 < 0:
			continue
		#print ('max: ', max(n1,n2))
		#print ('min: ', min(n1,n2))
		if p <= max(n1,n2):
			res += 1
		elif p <= min(n1,n2) + 1:
			res += 1
		elif S > 0:
			if p <= min(n1,n2) + 2:
				S-=1
				res+=1

	ans.writelines("Case #" + repr(k+1) + ': ' + repr(res) + '\n')

ans.close()
f.close()