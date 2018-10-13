def flip(arr, i, j):
	for k in range(i, j):
		if arr[k] == '-':
			arr[k] = '+'
		else:
			arr[k] = '-'

def minStep(arr, k):
	li = list(arr)
	i = 0
	count = 0
	while i < len(li)-k+1:
		if li[i] == '-':
			flip(li, i, i+k)
			count += 1
		i += 1
	
	while i < len(li):
		if li[i] == '-':
			count = -1
		i += 1
		
	return count
			
	
case = int(raw_input())
for c in range(1, case+1):
	arr, k = [s for s in raw_input().split(" ")]
	k = int(k)
	
	res = minStep(arr, k)
	if res != -1:
		print "Case #"+str(c)+": " + str(res)
	else:
		print "Case #"+str(c)+": IMPOSSIBLE"
		