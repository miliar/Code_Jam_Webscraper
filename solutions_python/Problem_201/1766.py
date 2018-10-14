import heapq

def getMinMax(k):
	if k%2 == 0:
		return (k/2, (k/2) -1)
	else:
		return ((k-1)/2,(k-1)/2)

def bathroom(n,k):
	myMax, myMin = getMinMax(n)
	if k == 1:
		return (myMax, myMin) 
	q = [myMax, myMin]
	count = 0
	while True:
		curr = q.pop(0)
		count += 1
		#left
		leftMax, leftMin = getMinMax(curr)
		if count == k-1:
			return (leftMax, leftMin)
		q.append(leftMax)
		q.append(leftMin)
		heapq._heapify_max(q)

def main():
	t = int(raw_input())
	for i in xrange(1, t+1):
		n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  		myMax, myMin = bathroom(n,k)
  		print "Case #{}: {} {}".format(i, myMax, myMin)

main()