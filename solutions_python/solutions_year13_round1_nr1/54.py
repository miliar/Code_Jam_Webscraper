def taken(r, num):
	sum = 0
	sum += (2*r + 1) * num
	sum += 2*(num)*(num-1)
	return sum
	
def numrings(r, t):
	low = 0
	high = 10**18+1
	while high-low>1 :
		mid = (low+high)/2
		if (taken(r, mid) <= t) :
			low = mid
		else :
			high = mid
	return low
	
input = [int(v) for v in open('in.txt').read().split()]
for i in range(input[0]):
	r = input[i*2+1]
	t = input[i*2+2]
	s = "Case #" + str(i+1) + ": " + str(numrings(r, t))
	print s
	